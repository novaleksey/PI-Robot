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
-- Name: PI-Robot; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE "PI-Robot" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';


\connect -reuse-previous=on "dbname='PI-Robot'"

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
-- Name: forumdata_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.forumdata_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 9999999
    CACHE 1;


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Forumdata; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Forumdata" (
    "@Forumdata" integer DEFAULT nextval('public.forumdata_id_seq'::regclass) NOT NULL,
    raw_content text,
    media text,
    seller_id integer NOT NULL,
    forumtheme_id integer NOT NULL
);


--
-- Name: forumtheme_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.forumtheme_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;


--
-- Name: Forumtheme; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Forumtheme" (
    "@Forumtheme" integer DEFAULT nextval('public.forumtheme_id_seq'::regclass) NOT NULL,
    seller integer,
    tradingplatform integer NOT NULL,
    url text NOT NULL,
    title text
);


--
-- Name: TABLE "Forumtheme"; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public."Forumtheme" IS 'Таблица ссылок на тему на форуме продавцов';


--
-- Name: profile_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1;


--
-- Name: Profile; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Profile" (
    "@Profile" integer DEFAULT nextval('public.profile_id_seq'::regclass) NOT NULL,
    seller integer NOT NULL,
    platform integer NOT NULL,
    url text,
    register_at date,
    status text,
    success_deal smallint NOT NULL,
    deposit integer NOT NULL
);


--
-- Name: TABLE "Profile"; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public."Profile" IS 'Карточка продавца на определенной площадке';


--
-- Name: qtask_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.qtask_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: Qtask; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Qtask" (
    "@Qtask" integer DEFAULT nextval('public.qtask_id_seq'::regclass) NOT NULL,
    kind text NOT NULL,
    params text,
    extra text,
    created_at timestamp without time zone DEFAULT now() NOT NULL,
    delayed_to timestamp without time zone,
    priority smallint NOT NULL,
    retries smallint DEFAULT 0 NOT NULL
);


--
-- Name: rawdata_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rawdata_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1;


--
-- Name: RawData; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."RawData" (
    "@RawData" integer DEFAULT nextval('public.rawdata_id_seq'::regclass) NOT NULL,
    hash text NOT NULL,
    source_id integer NOT NULL,
    external_url text NOT NULL,
    updated_at timestamp without time zone NOT NULL,
    "RawDataContent" integer NOT NULL
);


--
-- Name: rawdatacontent_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.rawdatacontent_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1;


--
-- Name: RawDataContent; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."RawDataContent" (
    "@RawDataContent" integer DEFAULT nextval('public.rawdatacontent_id_seq'::regclass) NOT NULL,
    content text NOT NULL
);


--
-- Name: seller_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.seller_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1;


--
-- Name: Seller; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Seller" (
    "@Seller" integer DEFAULT nextval('public.seller_id_seq'::regclass) NOT NULL,
    nickname text NOT NULL,
    worktype text,
    status integer,
    contacts text
);


--
-- Name: sellerstatus_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sellerstatus_id_seq
    START WITH 6
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 99999999
    CACHE 1;


--
-- Name: Sellerstatus; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Sellerstatus" (
    "@Sellerstatus" integer DEFAULT nextval('public.sellerstatus_id_seq'::regclass) NOT NULL,
    value text NOT NULL
);


--
-- Name: TABLE "Sellerstatus"; Type: COMMENT; Schema: public; Owner: -
--

COMMENT ON TABLE public."Sellerstatus" IS 'Статусы продавцов';


--
-- Name: tradingplatform_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.tradingplatform_id_seq
    START WITH 2
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 999999999
    CACHE 1;


--
-- Name: Tradingplatform; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Tradingplatform" (
    "@Tradingplatform" integer DEFAULT nextval('public.tradingplatform_id_seq'::regclass) NOT NULL,
    url text NOT NULL
);


--
-- Name: settings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.settings (
    option_name character varying(2044) NOT NULL,
    option_value character varying(2044) NOT NULL
);


--
-- Name: Seller Seller_nickname_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Seller"
    ADD CONSTRAINT "Seller_nickname_key" UNIQUE (nickname);


--
-- Name: Forumdata unique_Forumdata_@Forumdata; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumdata"
    ADD CONSTRAINT "unique_Forumdata_@Forumdata" UNIQUE ("@Forumdata");


--
-- Name: Forumtheme unique_Forumtheme_@Forumtheme; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumtheme"
    ADD CONSTRAINT "unique_Forumtheme_@Forumtheme" UNIQUE ("@Forumtheme");


--
-- Name: Profile unique_Profile_@Profile; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Profile"
    ADD CONSTRAINT "unique_Profile_@Profile" UNIQUE ("@Profile");


--
-- Name: Qtask unique_Qtask_@Qtask; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Qtask"
    ADD CONSTRAINT "unique_Qtask_@Qtask" UNIQUE ("@Qtask");


--
-- Name: RawDataContent unique_RawDataContent_@RawDataContent; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."RawDataContent"
    ADD CONSTRAINT "unique_RawDataContent_@RawDataContent" UNIQUE ("@RawDataContent");


--
-- Name: RawData unique_RawData_@RawData; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."RawData"
    ADD CONSTRAINT "unique_RawData_@RawData" UNIQUE ("@RawData");


--
-- Name: Seller unique_Seller_@Seller; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Seller"
    ADD CONSTRAINT "unique_Seller_@Seller" UNIQUE ("@Seller");


--
-- Name: Sellerstatus unique_Sellerstatus_@Sellerstatus; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Sellerstatus"
    ADD CONSTRAINT "unique_Sellerstatus_@Sellerstatus" UNIQUE ("@Sellerstatus");


--
-- Name: Tradingplatform unique_Tradingplatform_@Tradingplatform; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Tradingplatform"
    ADD CONSTRAINT "unique_Tradingplatform_@Tradingplatform" UNIQUE ("@Tradingplatform");


--
-- Name: settings unique_settings_option_name; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.settings
    ADD CONSTRAINT unique_settings_option_name UNIQUE (option_name);


--
-- Name: index_forumtheme_i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_forumtheme_i ON public."Forumdata" USING btree (forumtheme_id);


--
-- Name: index_platform; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_platform ON public."Profile" USING btree (platform);


--
-- Name: index_seller; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_seller ON public."Profile" USING btree (seller);


--
-- Name: index_seller1; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_seller1 ON public."Forumtheme" USING btree (seller);


--
-- Name: index_seller_i; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_seller_i ON public."Forumdata" USING btree (seller_id);


--
-- Name: index_tradingplatform; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX index_tradingplatform ON public."Forumtheme" USING btree (tradingplatform);


--
-- Name: Forumdata lnk_Forumtheme_Forumdata; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumdata"
    ADD CONSTRAINT "lnk_Forumtheme_Forumdata" FOREIGN KEY (forumtheme_id) REFERENCES public."Forumtheme"("@Forumtheme") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: RawData lnk_RawDataContent_RawData; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."RawData"
    ADD CONSTRAINT "lnk_RawDataContent_RawData" FOREIGN KEY ("RawDataContent") REFERENCES public."RawDataContent"("@RawDataContent") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Forumdata lnk_Seller_Forumdata; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumdata"
    ADD CONSTRAINT "lnk_Seller_Forumdata" FOREIGN KEY (seller_id) REFERENCES public."Seller"("@Seller") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Forumtheme lnk_Seller_Forumtheme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumtheme"
    ADD CONSTRAINT "lnk_Seller_Forumtheme" FOREIGN KEY (seller) REFERENCES public."Seller"("@Seller") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Profile lnk_Seller_Profile; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Profile"
    ADD CONSTRAINT "lnk_Seller_Profile" FOREIGN KEY (seller) REFERENCES public."Seller"("@Seller") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Seller lnk_Sellerstatus_Seller; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Seller"
    ADD CONSTRAINT "lnk_Sellerstatus_Seller" FOREIGN KEY (status) REFERENCES public."Sellerstatus"("@Sellerstatus") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Forumtheme lnk_Tradingplatform_Forumtheme; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Forumtheme"
    ADD CONSTRAINT "lnk_Tradingplatform_Forumtheme" FOREIGN KEY (tradingplatform) REFERENCES public."Tradingplatform"("@Tradingplatform") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Profile lnk_Tradingplatform_Profile; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Profile"
    ADD CONSTRAINT "lnk_Tradingplatform_Profile" FOREIGN KEY (platform) REFERENCES public."Tradingplatform"("@Tradingplatform") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: RawData lnk_Tradingplatform_RawData; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."RawData"
    ADD CONSTRAINT "lnk_Tradingplatform_RawData" FOREIGN KEY (source_id) REFERENCES public."Tradingplatform"("@Tradingplatform") MATCH FULL ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

