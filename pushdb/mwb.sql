--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

DROP TABLE public.pred;
SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: pred; Type: TABLE; Schema: public; Owner: andy; Tablespace: 
--

CREATE TABLE pred (
    hometeam character varying(80),
    awayteam character varying(80),
    result numeric,
    pred numeric,
    data_type character varying(30),
    matchdate date,
    commentary character varying(1000)
);


ALTER TABLE public.pred OWNER TO andy;

--
-- Data for Name: pred; Type: TABLE DATA; Schema: public; Owner: andy
--

COPY pred (hometeam, awayteam, result, pred, data_type, matchdate, commentary) FROM stdin;
Burton	Derby	0	14.14	FREG_PRED	2016-08-26	\N
Watford	Arsenal	0	-26.88	FREG_PRED	2016-08-27	\N
Everton	Stoke	0	51.52	FREG_PRED	2016-08-27	\N
Man City	West Ham	0	5.43	FREG_PRED	2016-08-28	\N
Leicester	Swansea	0	121.31	FREG_PRED	2016-08-27	Comfortable Home Win
Southampton	Sunderland	0	103.33	FREG_PRED	2016-08-27	Comfortable Home Win
West Ham	Bournemouth	0	81.2	FREG_PRED	2016-08-21	Tight Home Win
Tottenham	Liverpool	0	85.22	FREG_PRED	2016-08-27	Tight Home Win
Sunderland	Middlesbrough	0	-84.38	FREG_PRED	2016-08-21	Tight Away Win
Chelsea	Burnley	0	-89.52	FREG_PRED	2016-08-27	Tight Away Win
West Brom	Middlesbrough	0	-140.31	FREG_PRED	2016-08-28	Comfortable Away Win
Norwich	Leeds	0	28.23	RESULT	2016-11-05	\N
Bristol City	Brighton	0	35.37	RESULT	2016-11-05	\N
Chelsea	Everton	0	-1.91	RESULT	2016-11-05	\N
Huddersfield	Birmingham	0	34.8	RESULT	2016-11-05	\N
Bournemouth	Sunderland	0	35.75	RESULT	2016-11-05	\N
Man City	Middlesbrough	0	99.48	RESULT	2016-11-05	Tight Home Win
West Ham	Stoke	0	64.71	RESULT	2016-11-05	Tight Home Win
Arsenal	Tottenham	0	61.79	RESULT	2016-11-06	Tight Home Win
Wigan	Reading	0	70.72	RESULT	2016-11-05	Tight Home Win
Leicester	West Brom	0	74.54	RESULT	2016-11-06	Tight Home Win
Newcastle	Cardiff	0	91.15	RESULT	2016-11-05	Tight Home Win
Coventry	Chesterfield	0	270.21	GOALS	2016-11-01	Greater than 2.5 Goals
Hull	Southampton	0	252.41	GOALS	2016-11-06	Greater than 2.5 Goals
Liverpool	Watford	0	332.22	GOALS	2016-11-06	Greater than 2.5 Goals
Burton	Barnsley	0	260.19	GOALS	2016-11-05	Greater than 2.5 Goals
Aston Villa	Blackburn	0	325.03	GOALS	2016-11-05	Greater than 2.5 Goals
Southampton	Chelsea	0	225.41	GOALS	2016-10-30	Greater than 1.5 Goals
Stoke	Swansea	0	217.43	GOALS	2016-10-31	Greater than 1.5 Goals
Brentford	Fulham	0	222.3	GOALS	2016-11-04	Greater than 1.5 Goals
Wolves	Derby	0	214.71	GOALS	2016-11-05	Greater than 1.5 Goals
Rotherham	Preston	0	175.46	GOALS	2016-11-05	Greater than 1.5 Goals
Southampton	Chelsea	0	1.41	RESULT	2016-10-30	\N
Stoke	Swansea	0	6.59	RESULT	2016-10-31	\N
Coventry	Chesterfield	0	21.24	RESULT	2016-11-01	\N
Hull	Southampton	0	-14.76	RESULT	2016-11-06	\N
Burton	Barnsley	0	7.37	RESULT	2016-11-05	\N
Rotherham	Preston	0	19.62	RESULT	2016-11-05	\N
Aston Villa	Blackburn	0	18.32	RESULT	2016-11-05	\N
Brentford	Fulham	0	63.63	RESULT	2016-11-04	Tight Home Win
Liverpool	Watford	0	89.08	RESULT	2016-11-06	Tight Home Win
Wolves	Derby	0	-90.38	RESULT	2016-11-05	Tight Away Win
Chelsea	Everton	0	250.01	GOALS	2016-11-05	Greater than 2.5 Goals
Arsenal	Tottenham	0	274.07	GOALS	2016-11-06	Greater than 2.5 Goals
Bournemouth	Sunderland	0	280.23	GOALS	2016-11-05	Greater than 2.5 Goals
Newcastle	Cardiff	0	306.92	GOALS	2016-11-05	Greater than 2.5 Goals
Man City	Middlesbrough	0	227.1	GOALS	2016-11-05	Greater than 1.5 Goals
West Ham	Stoke	0	212.28	GOALS	2016-11-05	Greater than 1.5 Goals
Norwich	Leeds	0	235.09	GOALS	2016-11-05	Greater than 1.5 Goals
Bristol City	Brighton	0	238.23	GOALS	2016-11-05	Greater than 1.5 Goals
Huddersfield	Birmingham	0	197.27	GOALS	2016-11-05	Greater than 1.5 Goals
Wigan	Reading	0	215.94	GOALS	2016-11-05	Greater than 1.5 Goals
Leicester	West Brom	0	196.02	GOALS	2016-11-06	Greater than 1.5 Goals
\.


--
-- PostgreSQL database dump complete
--

