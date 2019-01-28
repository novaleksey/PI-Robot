--
-- PostgreSQL database dump
--

-- Dumped from database version 11.0 (Debian 11.0-1.pgdg90+2)
-- Dumped by pg_dump version 11.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: Sellerstatus; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Sellerstatus" VALUES (1, 'Не имеет');
INSERT INTO public."Sellerstatus" VALUES (2, 'Проверенный продавец');
INSERT INTO public."Sellerstatus" VALUES (3, 'Кидала');
INSERT INTO public."Sellerstatus" VALUES (4, 'Сомнительный');
INSERT INTO public."Sellerstatus" VALUES (5, 'Не работает');
INSERT INTO public."Sellerstatus" VALUES (6, 'Не проверен');

--
-- PostgreSQL database dump complete
--

