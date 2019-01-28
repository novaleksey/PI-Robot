import datetime

from sqlalchemy import select, or_

from Models.Task import Task


class QtaskCore:
    kind = NotImplemented
    schema = {}
    t = Task()

    def __init__(self, task_id, priority, params, created_at, delayed_to, extra, retries):
        self.task_id = task_id
        self.priority = priority
        self.params = params
        self.created_at = created_at
        self.delayed_to = delayed_to
        self.extra = extra
        self.retries = retries

    @classmethod
    def _get_kind(cls):
        if cls.kind is NotImplemented:
            raise NotImplementedError
        return cls.kind

    @classmethod
    def create(cls, params=None, delayed_to=None, priority=0, extra=None):
        kind = cls._get_kind()

        qtask = cls.t.TaskTable
        s = select([qtask]).\
            where(qtask.c.kind == kind).\
            where(qtask.c.params == params)
        res = cls.t.connect.execute(s).fetchone()
        if res:
            return cls(
                task_id=res[qtask.c.get(cls.t.PK)],
                created_at=res[qtask.c.created_at],
                retries=res[qtask.c.retries],
                priority=res[qtask.c.priority],
                params=res[qtask.c.params],
                extra=res[qtask.c.extra],
                delayed_to=res[qtask.c.delayed_to]
            )
        else:
            q = qtask.insert().returning(
                qtask.c.get(cls.t.PK),
                qtask.c.created_at,
                qtask.c.retries,
                qtask.c.priority,
                qtask.c.params,
                qtask.c.extra,
                qtask.c.delayed_to
            ).values(
                kind=kind,
                extra=extra,
                params=params,
                priority=priority,
                delayed_to=delayed_to
            )
            row = cls.t.connect.execute(q).fetchone()

            return cls(
                task_id=row[qtask.c.get(cls.t.PK)],
                created_at=row[qtask.c.created_at],
                retries=row[qtask.c.retries],
                priority=row[qtask.c.priority],
                params=row[qtask.c.params],
                extra=row[qtask.c.extra],
                delayed_to=row[qtask.c.delayed_to]
            )

    @classmethod
    def get_task(cls):
        kind = cls._get_kind()

        qtask = cls.t.TaskTable
        s = select([qtask]).\
            where(qtask.c.kind == kind).\
            where(
            or_(
                qtask.c.delayed_to < datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),
                qtask.c.delayed_to == None)).\
            order_by(qtask.c.priority.desc()).\
            limit(1)

        res = cls.t.connect.execute(s).fetchone()
        if res is None:
            return res
        return cls(
            task_id=res['@Qtask'],
            created_at=res['created_at'],
            retries=res['retries'],
            priority=res['priority'],
            params=res['params'],
            extra=res['extra'],
            delayed_to=res['delayed_to']
        )

    def delay_for(self, delay_time):
        delay_to = datetime.datetime.now() + delay_time
        upd = self.t.TaskTable.update().values(
            delayed_to=delay_to
        ).where(self.t.TaskTable.c.get(self.t.PK) == self.task_id)
        res = self.t.connect.execute(upd)
        return res

    def done(self):
        dlt = self.t.TaskTable.delete().\
            where(self.t.TaskTable.c.get(self.t.PK) == self.task_id)
        res = self.t.connect.execute(dlt)
        return res


