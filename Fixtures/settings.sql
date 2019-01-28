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
-- Data for Name: settings; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.settings VALUES ('Dublikat.Theme.Включено', '1');
INSERT INTO public.settings VALUES ('Dublikat.Collect.Включено', '1');
INSERT INTO public.settings VALUES ('Migalki.Theme.Включено', '1');
INSERT INTO public.settings VALUES ('Migalki.Collect.Включено', '1');
INSERT INTO public.settings VALUES ('SellerData.Loader.Включено', '1');
INSERT INTO public.settings VALUES ('RawData.Loader.Включено', '1');

--
-- PostgreSQL database dump complete
--
