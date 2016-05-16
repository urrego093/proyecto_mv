--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_cas; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_cas (
    id integer NOT NULL,
    user_id integer,
    created_on timestamp without time zone,
    service character varying(512),
    ticket character varying(512),
    renew character(1)
);


ALTER TABLE auth_cas OWNER TO udistrital;

--
-- Name: auth_cas_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_cas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_cas_id_seq OWNER TO udistrital;

--
-- Name: auth_cas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_cas_id_seq OWNED BY auth_cas.id;


--
-- Name: auth_event; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_event (
    id integer NOT NULL,
    time_stamp timestamp without time zone,
    client_ip character varying(512),
    user_id integer,
    origin character varying(512),
    description text
);


ALTER TABLE auth_event OWNER TO udistrital;

--
-- Name: auth_event_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_event_id_seq OWNER TO udistrital;

--
-- Name: auth_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_event_id_seq OWNED BY auth_event.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    role character varying(512),
    description text
);


ALTER TABLE auth_group OWNER TO udistrital;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_group_id_seq OWNER TO udistrital;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_membership; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_membership (
    id integer NOT NULL,
    user_id integer,
    group_id integer
);


ALTER TABLE auth_membership OWNER TO udistrital;

--
-- Name: auth_membership_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_membership_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_membership_id_seq OWNER TO udistrital;

--
-- Name: auth_membership_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_membership_id_seq OWNED BY auth_membership.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    group_id integer,
    name character varying(512),
    table_name character varying(512),
    record_id integer
);


ALTER TABLE auth_permission OWNER TO udistrital;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_permission_id_seq OWNER TO udistrital;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    first_name character varying(128),
    last_name character varying(128),
    email character varying(512),
    password character varying(512),
    registration_key character varying(512),
    reset_password_key character varying(512),
    registration_id character varying(512)
);


ALTER TABLE auth_user OWNER TO udistrital;

--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE auth_user_id_seq OWNER TO udistrital;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: course; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE course (
    id integer NOT NULL,
    code_course integer,
    name_course character varying(60),
    description_course text,
    is_active character(1),
    created_on timestamp without time zone,
    created_by integer,
    modified_on timestamp without time zone,
    modified_by integer
);


ALTER TABLE course OWNER TO udistrital;

--
-- Name: course_group; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE course_group (
    id integer NOT NULL,
    cod_group integer,
    id_teacher integer,
    cod_course integer,
    semester character varying(512),
    is_active character(1),
    created_on timestamp without time zone,
    created_by integer,
    modified_on timestamp without time zone,
    modified_by integer
);


ALTER TABLE course_group OWNER TO udistrital;

--
-- Name: course_group_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE course_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE course_group_id_seq OWNER TO udistrital;

--
-- Name: course_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE course_group_id_seq OWNED BY course_group.id;


--
-- Name: course_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE course_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE course_id_seq OWNER TO udistrital;

--
-- Name: course_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE course_id_seq OWNED BY course.id;


--
-- Name: job; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE job (
    id integer NOT NULL,
    name character varying(512),
    user_id integer,
    task_id character varying(512)
);


ALTER TABLE job OWNER TO udistrital;

--
-- Name: job_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE job_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE job_id_seq OWNER TO udistrital;

--
-- Name: job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE job_id_seq OWNED BY job.id;


--
-- Name: machine; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE machine (
    id integer NOT NULL,
    ip_machine character varying(512),
    code_course integer,
    operative_system character varying(512),
    memory character varying(512),
    processor character varying(512),
    description_machine text,
    is_active character(1),
    created_on timestamp without time zone,
    created_by integer,
    modified_on timestamp without time zone,
    modified_by integer
);


ALTER TABLE machine OWNER TO udistrital;

--
-- Name: machine_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE machine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE machine_id_seq OWNER TO udistrital;

--
-- Name: machine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE machine_id_seq OWNED BY machine.id;


--
-- Name: port_machine; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE port_machine (
    id integer NOT NULL,
    ip_machine integer,
    number_port character varying(512),
    hostname character varying(512),
    is_active character(1),
    created_on timestamp without time zone,
    created_by integer,
    modified_on timestamp without time zone,
    modified_by integer
);


ALTER TABLE port_machine OWNER TO udistrital;

--
-- Name: port_machine_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE port_machine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE port_machine_id_seq OWNER TO udistrital;

--
-- Name: port_machine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE port_machine_id_seq OWNED BY port_machine.id;


--
-- Name: scheduler_run; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE scheduler_run (
    id integer NOT NULL,
    task_id integer,
    status character varying(512),
    start_time timestamp without time zone,
    stop_time timestamp without time zone,
    run_output text,
    run_result text,
    traceback text,
    worker_name character varying(512)
);


ALTER TABLE scheduler_run OWNER TO udistrital;

--
-- Name: scheduler_run_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE scheduler_run_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE scheduler_run_id_seq OWNER TO udistrital;

--
-- Name: scheduler_run_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE scheduler_run_id_seq OWNED BY scheduler_run.id;


--
-- Name: scheduler_task; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE scheduler_task (
    id integer NOT NULL,
    application_name character varying(512),
    task_name character varying(512),
    group_name character varying(512),
    status character varying(512),
    function_name character varying(512),
    uuid character varying(255),
    args text,
    vars text,
    enabled character(1),
    start_time timestamp without time zone,
    next_run_time timestamp without time zone,
    stop_time timestamp without time zone,
    repeats integer,
    retry_failed integer,
    period integer,
    prevent_drift character(1),
    timeout integer,
    sync_output integer,
    times_run integer,
    times_failed integer,
    last_run_time timestamp without time zone,
    assigned_worker_name character varying(512)
);


ALTER TABLE scheduler_task OWNER TO udistrital;

--
-- Name: scheduler_task_deps; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE scheduler_task_deps (
    id integer NOT NULL,
    job_name character varying(512),
    task_parent integer,
    task_child integer,
    can_visit character(1)
);


ALTER TABLE scheduler_task_deps OWNER TO udistrital;

--
-- Name: scheduler_task_deps_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE scheduler_task_deps_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE scheduler_task_deps_id_seq OWNER TO udistrital;

--
-- Name: scheduler_task_deps_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE scheduler_task_deps_id_seq OWNED BY scheduler_task_deps.id;


--
-- Name: scheduler_task_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE scheduler_task_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE scheduler_task_id_seq OWNER TO udistrital;

--
-- Name: scheduler_task_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE scheduler_task_id_seq OWNED BY scheduler_task.id;


--
-- Name: scheduler_worker; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE scheduler_worker (
    id integer NOT NULL,
    worker_name character varying(255),
    first_heartbeat timestamp without time zone,
    last_heartbeat timestamp without time zone,
    status character varying(512),
    is_ticker character(1),
    group_names text,
    worker_stats json
);


ALTER TABLE scheduler_worker OWNER TO udistrital;

--
-- Name: scheduler_worker_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE scheduler_worker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE scheduler_worker_id_seq OWNER TO udistrital;

--
-- Name: scheduler_worker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE scheduler_worker_id_seq OWNED BY scheduler_worker.id;


--
-- Name: student_x_machine; Type: TABLE; Schema: public; Owner: udistrital; Tablespace: 
--

CREATE TABLE student_x_machine (
    id integer NOT NULL,
    ip_machine integer,
    code_student character varying(512),
    name_student character varying(512),
    semester character varying(512),
    is_active character(1),
    created_on timestamp without time zone,
    created_by integer,
    modified_on timestamp without time zone,
    modified_by integer
);


ALTER TABLE student_x_machine OWNER TO udistrital;

--
-- Name: student_x_machine_id_seq; Type: SEQUENCE; Schema: public; Owner: udistrital
--

CREATE SEQUENCE student_x_machine_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE student_x_machine_id_seq OWNER TO udistrital;

--
-- Name: student_x_machine_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: udistrital
--

ALTER SEQUENCE student_x_machine_id_seq OWNED BY student_x_machine.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_cas ALTER COLUMN id SET DEFAULT nextval('auth_cas_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_event ALTER COLUMN id SET DEFAULT nextval('auth_event_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_membership ALTER COLUMN id SET DEFAULT nextval('auth_membership_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course ALTER COLUMN id SET DEFAULT nextval('course_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course_group ALTER COLUMN id SET DEFAULT nextval('course_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY job ALTER COLUMN id SET DEFAULT nextval('job_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY machine ALTER COLUMN id SET DEFAULT nextval('machine_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY port_machine ALTER COLUMN id SET DEFAULT nextval('port_machine_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_run ALTER COLUMN id SET DEFAULT nextval('scheduler_run_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_task ALTER COLUMN id SET DEFAULT nextval('scheduler_task_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_task_deps ALTER COLUMN id SET DEFAULT nextval('scheduler_task_deps_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_worker ALTER COLUMN id SET DEFAULT nextval('scheduler_worker_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY student_x_machine ALTER COLUMN id SET DEFAULT nextval('student_x_machine_id_seq'::regclass);


--
-- Data for Name: auth_cas; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_cas (id, user_id, created_on, service, ticket, renew) FROM stdin;
\.


--
-- Name: auth_cas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_cas_id_seq', 1, false);


--
-- Data for Name: auth_event; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_event (id, time_stamp, client_ip, user_id, origin, description) FROM stdin;
1	2016-03-23 15:08:49	127.0.0.1	\N	auth	Group 3 created
2	2016-03-23 15:08:49	127.0.0.1	\N	auth	User 1 Registered
3	2016-03-23 15:09:38	127.0.0.1	\N	auth	Group 4 created
4	2016-03-23 15:09:38	127.0.0.1	\N	auth	User 2 Registered
5	2016-03-23 15:09:47	127.0.0.1	1	auth	User 1 Logged-in
6	2016-03-23 15:10:54	127.0.0.1	1	auth	User 1 Logged-out
7	2016-03-23 15:17:14	127.0.0.1	1	auth	User 1 Logged-in
8	2016-03-24 13:58:47	127.0.0.1	1	auth	User 1 Logged-in
9	2016-03-24 14:01:09	127.0.0.1	\N	auth	Group 5 created
10	2016-03-24 14:01:09	127.0.0.1	\N	auth	User 3 Registered
11	2016-03-24 14:15:08	127.0.0.1	\N	auth	Group 6 created
12	2016-03-24 14:15:08	127.0.0.1	\N	auth	User 4 Registered
13	2016-03-24 14:23:38	127.0.0.1	\N	auth	Group 7 created
14	2016-03-24 14:23:38	127.0.0.1	\N	auth	User 5 Registered
15	2016-03-24 14:24:06	127.0.0.1	\N	auth	Group 8 created
16	2016-03-24 14:24:06	127.0.0.1	\N	auth	User 6 Registered
17	2016-03-24 14:36:27	127.0.0.1	\N	auth	Group 9 created
18	2016-03-24 14:36:27	127.0.0.1	\N	auth	User 7 Registered
19	2016-03-24 14:40:13	127.0.0.1	\N	auth	Group 10 created
20	2016-03-24 14:40:13	127.0.0.1	\N	auth	User 8 Registered
21	2016-03-24 14:40:41	127.0.0.1	\N	auth	Group 11 created
22	2016-03-24 14:40:41	127.0.0.1	\N	auth	User 9 Registered
23	2016-03-24 14:41:02	127.0.0.1	\N	auth	Group 12 created
24	2016-03-24 14:41:02	127.0.0.1	\N	auth	User 10 Registered
25	2016-04-08 14:37:17	127.0.0.1	1	auth	User 1 Logged-in
26	2016-04-14 12:25:47	127.0.0.1	1	auth	User 1 Logged-in
27	2016-04-14 15:41:18	127.0.0.1	1	auth	User 1 Logged-in
28	2016-04-15 20:40:22	127.0.0.1	1	auth	User 1 Logged-in
29	2016-04-18 10:23:07	127.0.0.1	1	auth	User 1 Logged-in
30	2016-04-21 13:30:49	127.0.0.1	1	auth	User 1 Logged-in
31	2016-04-21 14:17:08	127.0.0.1	1	auth	User 1 Logged-in
32	2016-04-21 21:37:00	127.0.0.1	1	auth	User 1 Logged-in
33	2016-04-21 21:51:57	127.0.0.1	1	auth	User 1 Logged-out
34	2016-04-21 21:53:28	127.0.0.1	\N	auth	Group 13 created
35	2016-04-21 21:53:28	127.0.0.1	\N	auth	User 11 Registered
36	2016-04-21 21:53:47	127.0.0.1	1	auth	User 1 Logged-in
37	2016-04-21 22:00:07	127.0.0.1	1	auth	User 1 Logged-out
38	2016-04-21 22:00:24	127.0.0.1	11	auth	User 11 Logged-in
39	2016-04-21 22:01:29	127.0.0.1	11	auth	User 11 Logged-out
40	2016-04-21 22:03:12	127.0.0.1	1	auth	User 1 Logged-in
41	2016-04-21 22:07:14	127.0.0.1	1	auth	User 1 Logged-out
42	2016-04-21 22:39:49	127.0.0.1	1	auth	User 1 Logged-in
43	2016-04-21 22:39:52	127.0.0.1	1	auth	User 1 Logged-out
44	2016-04-21 22:40:10	127.0.0.1	11	auth	User 11 Logged-in
45	2016-04-22 11:07:18	127.0.0.1	11	auth	User 11 Logged-in
46	2016-04-22 11:38:32	127.0.0.1	11	auth	User 11 Logged-out
47	2016-04-22 11:38:39	127.0.0.1	1	auth	User 1 Logged-in
48	2016-04-22 11:39:57	127.0.0.1	1	auth	User 1 Logged-out
49	2016-04-22 11:40:21	127.0.0.1	1	auth	User 1 Logged-in
50	2016-04-22 11:40:32	127.0.0.1	1	auth	User 1 Logged-out
51	2016-04-22 11:41:17	127.0.0.1	11	auth	User 11 Logged-in
52	2016-04-22 11:44:29	127.0.0.1	11	auth	User 11 Logged-out
53	2016-04-22 11:51:40	127.0.0.1	1	auth	User 1 Logged-in
54	2016-04-22 11:55:21	127.0.0.1	1	auth	User 1 Logged-out
55	2016-04-22 11:55:30	127.0.0.1	11	auth	User 11 Logged-in
56	2016-04-22 12:21:50	127.0.0.1	11	auth	User 11 Logged-out
57	2016-04-22 12:21:56	127.0.0.1	11	auth	User 11 Logged-in
58	2016-04-22 22:23:38	127.0.0.1	1	auth	User 1 Logged-in
59	2016-04-22 22:32:03	127.0.0.1	1	auth	User 1 Logged-out
60	2016-04-22 22:32:13	127.0.0.1	11	auth	User 11 Logged-in
61	2016-04-26 11:42:38	127.0.0.1	11	auth	User 11 Logged-in
62	2016-04-26 11:47:14	127.0.0.1	1	auth	User 1 Logged-in
\.


--
-- Name: auth_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_event_id_seq', 62, true);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_group (id, role, description) FROM stdin;
1	administrador	Este es el administrador de la base de datos.
2	docente	Estos son los profesores de la base de datos
3	user_1	Grupo asignado únicamente al usuario 1
4	user_2	Grupo asignado únicamente al usuario 2
5	user_3	Grupo asignado únicamente al usuario 3
6	user_4	Grupo asignado únicamente al usuario 4
7	user_5	Grupo asignado únicamente al usuario 5
8	user_6	Grupo asignado únicamente al usuario 6
9	user_7	Grupo asignado únicamente al usuario 7
10	user_8	Grupo asignado únicamente al usuario 8
11	user_9	Grupo asignado únicamente al usuario 9
12	user_10	Grupo asignado únicamente al usuario 10
13	user_11	Grupo asignado únicamente al usuario 11
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_group_id_seq', 13, true);


--
-- Data for Name: auth_membership; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_membership (id, user_id, group_id) FROM stdin;
1	1	1
9	9	2
11	11	2
\.


--
-- Name: auth_membership_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_membership_id_seq', 11, true);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_permission (id, group_id, name, table_name, record_id) FROM stdin;
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_permission_id_seq', 1, false);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY auth_user (id, first_name, last_name, email, password, registration_key, reset_password_key, registration_id) FROM stdin;
11	Eduardo	Suarez	uno@gmail.com	pbkdf2(1000,20,sha512)$8fd4e73c04d3d0c9$f3b3bada0e9853bb4941334e4689a15b2e5c8553			
1	Carlos	Suarez	suarezsilvestre1@gmail.com	pbkdf2(1000,20,sha512)$9959f66fceacd8c6$e1c52f60fa35e78d48fe77e02ee25b6042f16022			
9	Carlos	Segundo	segundo@gmail.com	pbkdf2(1000,20,sha512)$9c1346263a9ad4b8$b9f02cf4e94e8f99c872c881d2e713508793937d			
\.


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('auth_user_id_seq', 11, true);


--
-- Data for Name: course; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY course (id, code_course, name_course, description_course, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
1	501	Modelos de Programacion I	Es es modelos I	T	2016-04-08 14:33:19	1	2016-04-08 14:33:19	1
2	503	Programacion Avanzada	Es el curso de programación avanzada que se realizara en tal y tal horario.	T	2016-04-18 10:32:46	1	2016-04-18 10:32:46	1
3	504	Programacion Basica	Es programacion Basica	T	2016-04-22 11:52:09	1	2016-04-22 11:52:09	1
\.


--
-- Data for Name: course_group; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY course_group (id, cod_group, id_teacher, cod_course, semester, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
1	81	11	1	2016-I	T	2016-04-21 15:14:32	1	2016-04-21 15:14:32	1
2	82	11	2	2016-I	T	2016-04-21 15:14:49	1	2016-04-21 15:14:49	1
3	83	11	3	2016-I	T	2016-04-21 15:15:04	1	2016-04-21 15:15:04	1
\.


--
-- Name: course_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('course_group_id_seq', 3, true);


--
-- Name: course_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('course_id_seq', 3, true);


--
-- Data for Name: job; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY job (id, name, user_id, task_id) FROM stdin;
1	None_0	\N	\N
2	None_1	\N	\N
3	None_2	\N	\N
4	1_0	1	\N
5	1_1	1	\N
6	1_2	1	\N
7	1_3	1	\N
8	1_4	1	\N
9	1_5	1	\N
10	1_6	1	1
11	1_7	1	\N
12	1_8	1	\N
13	1_9	1	2
14	1_10	1	3
15	1_11	1	4
16	1_12	1	5
17	1_13	1	6
18	1_14	1	\N
19	1_15	1	\N
20	1_16	1	\N
21	1_17	1	\N
22	1_18	1	\N
23	1_19	1	7
24	1_20	1	\N
25	1_21	1	\N
26	1_22	1	8
27	1_23	1	\N
28	1_24	1	\N
29	1_25	1	\N
30	1_26	1	9
31	1_27	1	10
32	1_28	1	11
33	1_29	1	12
34	1_30	1	13
35	1_31	1	\N
36	1_32	1	\N
37	1_33	1	\N
38	1_34	1	14
39	None_3	\N	15
40	None_4	\N	\N
41	None_5	\N	16
42	None_6	\N	\N
43	None_7	\N	\N
44	None_8	\N	\N
45	None_9	\N	\N
46	None_10	\N	17
47	None_11	\N	18
48	None_12	\N	19
49	None_13	\N	20
50	None_14	\N	21
51	None_15	\N	22
52	None_16	\N	23
53	None_17	\N	24
54	None_18	\N	25
55	None_19	\N	26
56	None_20	\N	27
57	None_21	\N	28
58	None_22	\N	29
59	None_23	\N	30
60	None_24	\N	31
61	None_25	\N	32
62	1_35	1	\N
63	1_36	1	33
\.


--
-- Name: job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('job_id_seq', 63, true);


--
-- Data for Name: machine; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY machine (id, ip_machine, code_course, operative_system, memory, processor, description_machine, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
1	192.168.1.63	1	Ubuntu	3072MB	5	Es la maquina de Carlos	T	2016-04-08 14:34:00	1	2016-04-08 14:34:00	1
2	192.168.1.62	1	CentOs	3072MB	4	Es la maquina de centos de Carlos	T	2016-04-14 12:24:53	1	2016-04-14 12:24:53	1
3	192.168.1.114	2	CentOs	5120MB	5	Tercera Maquina	T	2016-04-22 11:39:14	1	2016-04-22 11:39:14	1
4	192.168.1.115	3	CentOs	5120MB	5	maquina de prueba	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
\.


--
-- Name: machine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('machine_id_seq', 4, true);


--
-- Data for Name: port_machine; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY port_machine (id, ip_machine, number_port, hostname, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
1	4	5901	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
2	4	5902	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
3	4	5903	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
4	4	5904	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
5	4	5905	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
6	4	5906	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
7	4	5907	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
8	4	5908	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
9	4	5909	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
10	4	5910	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
11	4	5911	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
12	4	5912	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
13	4	5913	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
14	4	5914	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
15	4	5915	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
16	4	5916	\N	T	2016-04-26 11:59:28	1	2016-04-26 11:59:28	1
\.


--
-- Name: port_machine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('port_machine_id_seq', 16, true);


--
-- Data for Name: scheduler_run; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY scheduler_run (id, task_id, status, start_time, stop_time, run_output, run_result, traceback, worker_name) FROM stdin;
1	1	FAILED	2016-04-14 14:52:01	2016-04-14 14:52:12	('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 96, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11002
2	2	FAILED	2016-04-14 14:56:34	2016-04-14 14:56:45	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11002
3	3	FAILED	2016-04-14 14:58:21	2016-04-14 14:58:32	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11002
4	4	FAILED	2016-04-14 15:00:08	2016-04-14 15:00:18	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11002
16	16	FAILED	2016-04-15 16:32:38	2016-04-15 16:32:38	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3938
17	17	FAILED	2016-04-15 17:26:44	2016-04-15 17:26:44	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 63, in _convert\n    in zip(node.keys, node.values))\n  File "/usr/lib64/python2.7/ast.py", line 62, in <genexpr>\n    return dict((_convert(k), _convert(v)) for k, v\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3938
5	5	FAILED	2016-04-14 15:02:55	2016-04-14 15:03:06	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11002
6	6	FAILED	2016-04-14 15:09:39	2016-04-14 15:09:50	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nok: [192.168.1.62]\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nfatal: [192.168.1.62] => SSH Error: Shared connection to 192.168.1.62 closed.\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nFATAL: all hosts have already failed -- aborting\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/root/reiniciar.retry\\n\\n192.168.1.62               : ok=1    changed=0    unreachable=2    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#11792
7	7	FAILED	2016-04-14 15:45:59	2016-04-14 15:46:12	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Mostrar clave] ********************************************************* \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#3258
8	8	FAILED	2016-04-14 15:47:00	2016-04-14 15:47:11	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Mostrar clave] ********************************************************* \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#3258
18	18	FAILED	2016-04-15 17:31:03	2016-04-15 17:31:03	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 63, in _convert\n    in zip(node.keys, node.values))\n  File "/usr/lib64/python2.7/ast.py", line 62, in <genexpr>\n    return dict((_convert(k), _convert(v)) for k, v\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3938
9	9	FAILED	2016-04-14 16:23:37	2016-04-14 16:23:49	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nok: [192.168.1.62]\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Mostrar clave] ********************************************************* \\nok: [192.168.1.62] => {\\n    "var": {\\n        "ansible_become_pass": "reverse"\\n    }\\n}\\n\\nTASK: [Mostrar usuario] ******************************************************* \\nok: [192.168.1.62] => {\\n    "var": {\\n        "ansible_user": "centos"\\n    }\\n}\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nfatal: [192.168.1.62] => SSH Error: Shared connection to 192.168.1.62 closed.\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nFATAL: all hosts have already failed -- aborting\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=3    changed=0    unreachable=2    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 97, in playbook\n    guardar_resumen(nombre, str_salida[1])\nIndexError: list index out of range\n	localhost.localdomain#3258
10	10	COMPLETED	2016-04-14 16:27:56	2016-04-14 16:28:07	entro al playbook\n('\\nPLAY [Reiniciar una maquina] ************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nok: [192.168.1.62]\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Mostrar clave] ********************************************************* \\nok: [192.168.1.62] => {\\n    "var": {\\n        "ansible_become_pass": "reverse"\\n    }\\n}\\n\\nTASK: [Mostrar usuario] ******************************************************* \\nok: [192.168.1.62] => {\\n    "var": {\\n        "ansible_user": "centos"\\n    }\\n}\\n\\nTASK: [reiniciar maquina] ***************************************************** \\nfatal: [192.168.1.62] => SSH Error: Shared connection to 192.168.1.62 closed.\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nFATAL: all hosts have already failed -- aborting\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/reiniciar.retry\\n\\n192.168.1.62               : ok=3    changed=0    unreachable=2    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#3258
11	11	COMPLETED	2016-04-14 16:35:03	2016-04-14 16:35:14	entro al playbook\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nok: [192.168.1.62]\\nfatal: [192.168.1.63] => SSH Error: Permission denied (publickey,password).\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [usercreate | Creating user "Carlos" with admin access] ***************** \\nskipping: [192.168.1.62]\\n\\nTASK: [usercreate | Creating users "Carlos" without admin access] ************* \\nchanged: [192.168.1.62]\\n\\nTASK: [userdel | Deleating user "Carlos"] ************************************* \\nskipping: [192.168.1.62]\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/linux_users.retry\\n\\n192.168.1.62               : ok=2    changed=1    unreachable=0    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#3258
12	12	FAILED	2016-04-14 22:10:47	2016-04-14 22:10:48	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3258
13	13	FAILED	2016-04-14 22:48:06	2016-04-14 22:48:06	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3258
14	14	FAILED	2016-04-14 22:56:32	2016-04-14 22:56:32	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3258
15	15	FAILED	2016-04-15 16:12:15	2016-04-15 16:12:16	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3938
19	19	FAILED	2016-04-15 17:35:37	2016-04-15 17:35:37	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 63, in _convert\n    in zip(node.keys, node.values))\n  File "/usr/lib64/python2.7/ast.py", line 62, in <genexpr>\n    return dict((_convert(k), _convert(v)) for k, v\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#3938
20	20	FAILED	2016-04-15 17:59:01	2016-04-15 17:59:01	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 49, in literal_eval\n    node_or_string = parse(node_or_string, mode='eval')\n  File "/usr/lib64/python2.7/ast.py", line 37, in parse\n    return compile(source, filename, mode, PyCF_ONLY_AST)\n  File "<unknown>", line 1\n    origen=FieldStorage('archivo', 'Archivo.txt', '')somelist=['Carlos', 'centos']\n          ^\nSyntaxError: invalid syntax\n	localhost.localdomain#3938
21	21	FAILED	2016-04-15 18:02:34	2016-04-15 18:02:35	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 49, in literal_eval\n    node_or_string = parse(node_or_string, mode='eval')\n  File "/usr/lib64/python2.7/ast.py", line 37, in parse\n    return compile(source, filename, mode, PyCF_ONLY_AST)\n  File "<unknown>", line 1\n    origen=FieldStorage('archivo', 'Archivo.txt', '')somelist=['Carlos', 'centos']\n          ^\nSyntaxError: invalid syntax\n	localhost.localdomain#3938
22	22	FAILED	2016-04-15 18:23:44	2016-04-15 18:23:44	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 49, in literal_eval\n    node_or_string = parse(node_or_string, mode='eval')\n  File "/usr/lib64/python2.7/ast.py", line 37, in parse\n    return compile(source, filename, mode, PyCF_ONLY_AST)\n  File "<unknown>", line 1\n    origen=somelist=['Carlos', 'centos']\n          ^\nSyntaxError: invalid syntax\n	localhost.localdomain#6218
23	23	FAILED	2016-04-15 18:35:10	2016-04-15 18:35:10	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 49, in literal_eval\n    node_or_string = parse(node_or_string, mode='eval')\n  File "/usr/lib64/python2.7/ast.py", line 37, in parse\n    return compile(source, filename, mode, PyCF_ONLY_AST)\n  File "<unknown>", line 1\n    origen=somelist=['Carlos', 'centos']\n          ^\nSyntaxError: invalid syntax\n	localhost.localdomain#6218
24	24	FAILED	2016-04-15 18:36:26	2016-04-15 18:36:26	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 49, in literal_eval\n    node_or_string = parse(node_or_string, mode='eval')\n  File "/usr/lib64/python2.7/ast.py", line 37, in parse\n    return compile(source, filename, mode, PyCF_ONLY_AST)\n  File "<unknown>", line 1\n    origen=somelist=['Carlos', 'centos']\n          ^\nSyntaxError: invalid syntax\n	localhost.localdomain#6218
25	25	FAILED	2016-04-15 18:37:44	2016-04-15 18:37:44	entro al playbook\n	\N	Traceback (most recent call last):\n  File "/home/Carlos/Descargas/web2py/gluon/scheduler.py", line 315, in executor\n    result = dumps(_function(*args, **vars))\n  File "applications/datos/models/scheduler.py", line 78, in playbook\n    ruta_variables = escribir_variables_yml(ruta_variables, variables)\n  File "applications/datos/models/scheduler.py", line 30, in escribir_variables_yml\n    diccionario = ast.literal_eval(variables)\n  File "/usr/lib64/python2.7/ast.py", line 80, in literal_eval\n    return _convert(node_or_string)\n  File "/usr/lib64/python2.7/ast.py", line 79, in _convert\n    raise ValueError('malformed string')\nValueError: malformed string\n	localhost.localdomain#6218
31	31	COMPLETED	2016-04-15 20:24:05	2016-04-15 20:24:15	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_24.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nok: [192.168.1.62]\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nchanged: [192.168.1.62] => (item=Carlos)\\nchanged: [192.168.1.62] => (item=centos)\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=2    changed=1    unreachable=0    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
26	26	COMPLETED	2016-04-15 18:42:33	2016-04-15 18:42:39	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_19.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: ssh: connect to host 192.168.1.62 port 22: No route to host\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
27	27	COMPLETED	2016-04-15 19:28:21	2016-04-15 19:28:25	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_20.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.62] => SSH Error: ssh: connect to host 192.168.1.62 port 22: No route to host\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
28	28	COMPLETED	2016-04-15 19:29:07	2016-04-15 19:29:10	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_21.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.62] => SSH Error: ssh: connect to host 192.168.1.62 port 22: No route to host\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
29	29	COMPLETED	2016-04-15 20:12:52	2016-04-15 20:12:55	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_22.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.62] => SSH Error: ssh: connect to host 192.168.1.62 port 22: No route to host\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
30	30	COMPLETED	2016-04-15 20:16:56	2016-04-15 20:17:00	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_23.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nfatal: [192.168.1.62] => SSH Error: ssh: connect to host 192.168.1.62 port 22: No route to host\\n    while connecting to 192.168.1.62:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nFATAL: no hosts matched or all hosts have already failed -- aborting\\n\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=0    changed=0    unreachable=1    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
32	32	COMPLETED	2016-04-15 20:33:14	2016-04-15 20:33:23	entro al playbook\n --extra-vars @/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_25.yml\n('\\nPLAY [all] ******************************************************************** \\n\\nGATHERING FACTS *************************************************************** \\nfatal: [192.168.1.63] => SSH Error: ssh: connect to host 192.168.1.63 port 22: No route to host\\n    while connecting to 192.168.1.63:22\\nIt is sometimes useful to re-run the command using -vvvv, which prints SSH debug output to help diagnose the issue.\\nok: [192.168.1.62]\\n\\nTASK: [Copiar archivo a una maquina] ****************************************** \\nchanged: [192.168.1.62] => (item=Carlos)\\nchanged: [192.168.1.62] => (item=centos)\\n\\nPLAY RECAP ******************************************************************** \\n           to retry, use: --limit @/home/Carlos/copiarArchivo.retry\\n\\n192.168.1.62               : ok=2    changed=1    unreachable=0    failed=0   \\n192.168.1.63               : ok=0    changed=0    unreachable=1    failed=0   \\n\\n', '')\n	1	\N	localhost.localdomain#6218
\.


--
-- Name: scheduler_run_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('scheduler_run_id_seq', 32, true);


--
-- Data for Name: scheduler_task; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY scheduler_task (id, application_name, task_name, group_name, status, function_name, uuid, args, vars, enabled, start_time, next_run_time, stop_time, repeats, retry_failed, period, prevent_drift, timeout, sync_output, times_run, times_failed, last_run_time, assigned_worker_name) FROM stdin;
7	datos/maquinas	playbook	main	FAILED	playbook	24b887a5-5711-4388-836e-cd5c3ba1ab9e	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_19", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_19", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_19", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 15:45:52	2016-04-14 15:46:59	\N	1	0	60	F	120	0	0	1	2016-04-14 15:45:59	localhost.localdomain#3258
1	datos/maquinas	playbook	main	FAILED	playbook	1b809227-ca14-4b96-b661-58d69420a046	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_6", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_6", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_6", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 14:51:54	2016-04-14 14:53:01	\N	1	0	60	F	120	0	0	1	2016-04-14 14:52:01	localhost.localdomain#11002
4	datos/maquinas	playbook	main	FAILED	playbook	6e5191e7-df9e-40cf-b497-1e056f1f4f82	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_11", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_11", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_11", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 14:59:52	2016-04-14 15:01:08	\N	1	0	60	F	120	0	0	1	2016-04-14 15:00:08	localhost.localdomain#11002
2	datos/maquinas	playbook	main	FAILED	playbook	ff0c931c-d1e2-4edb-94e3-d72d4288dfbc	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_9", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_9", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_9", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 14:56:27	2016-04-14 14:57:34	\N	1	0	60	F	120	0	0	1	2016-04-14 14:56:34	localhost.localdomain#11002
6	datos/maquinas	playbook	main	FAILED	playbook	9d2aebf7-1fce-4cc3-85df-fb7a7e595326	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_13", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_13", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_13", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 15:09:33	2016-04-14 15:10:39	\N	1	0	60	F	120	0	0	1	2016-04-14 15:09:39	localhost.localdomain#11792
3	datos/maquinas	playbook	main	FAILED	playbook	65ea1d3d-fbb1-49de-9806-e8fdc892a3b3	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_10", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_10", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_10", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 14:58:13	2016-04-14 14:59:21	\N	1	0	60	F	120	0	0	1	2016-04-14 14:58:21	localhost.localdomain#11002
5	datos/maquinas	playbook	main	FAILED	playbook	9b03db0a-c81b-437d-a2eb-23ebc08bc6d8	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_12", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_12", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_12", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 15:02:45	2016-04-14 15:03:55	\N	1	0	60	F	120	0	0	1	2016-04-14 15:02:55	localhost.localdomain#11002
10	datos/maquinas	playbook	main	COMPLETED	playbook	fad6dab0-6b9e-4f8d-a320-de5c8532543a	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_27", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_27", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_27", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 16:27:41	2016-04-14 16:28:56	\N	1	0	60	F	120	0	1	0	2016-04-14 16:27:56	localhost.localdomain#3258
8	datos/maquinas	playbook	main	FAILED	playbook	02a7a876-660e-4e71-ac30-ecd398a7d2c2	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_22", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_22", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_22", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 15:46:51	2016-04-14 15:48:00	\N	1	0	60	F	120	0	0	1	2016-04-14 15:47:00	localhost.localdomain#3258
9	datos/maquinas	playbook	main	FAILED	playbook	c55ce0f2-2c73-47ad-ac61-9284de9a829d	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_26", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_26", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_26", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-14 16:23:25	2016-04-14 16:24:37	\N	1	0	60	F	120	0	0	1	2016-04-14 16:23:37	localhost.localdomain#3258
11	datos/maquinas	playbook	main	COMPLETED	playbook	302bcc23-b99b-4274-85fa-0aeb2f1b1134	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_28", "variables": "{'action': 'create_user', 'admin': 'no', 'username': 'Carlos', 'password': 'Crema112', 'remote': 'all'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_28", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_28", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/usuarios/linux_users.yml"}	T	2016-04-14 16:34:50	2016-04-14 16:36:03	\N	1	0	60	F	120	0	1	0	2016-04-14 16:35:03	localhost.localdomain#3258
14	datos/maquinas	playbook	main	FAILED	playbook	31a27921-483a-4c22-9fc4-c9943d9f8e3f	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_34", "variables": ["root", "estudiante1", "estudiante2", "estudiante3", "estudiante4", "estudiante5", "estudiante6", "estudiante7", "estudiante8", "estudiante9", "estudiante10", "estudiante11", "estudiante12", "estudiante13", "estudiante14", "estudiante15"], "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_34", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_34", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-14 22:56:23	2016-04-14 22:57:32	\N	1	0	60	F	120	0	0	1	2016-04-14 22:56:32	localhost.localdomain#3258
12	datos/maquinas	playbook	main	FAILED	playbook	02382dee-31fe-4b9b-a055-05a70173908c	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_29", "variables": ["root", "estudiante1", "estudiante2", "estudiante3", "estudiante4", "estudiante5", "estudiante6", "estudiante7", "estudiante8", "estudiante9", "estudiante10", "estudiante11", "estudiante12", "estudiante13", "estudiante14", "estudiante15"], "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_29", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_29", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-14 22:10:36	2016-04-14 22:11:47	\N	1	0	60	F	120	0	0	1	2016-04-14 22:10:47	localhost.localdomain#3258
13	datos/maquinas	playbook	main	FAILED	playbook	53ebcd41-5c8b-43a1-aea7-71fdb9687692	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_30", "variables": ["root", "estudiante1", "estudiante2", "estudiante3", "estudiante4", "estudiante5", "estudiante6", "estudiante7", "estudiante8", "estudiante9", "estudiante10", "estudiante11", "estudiante12", "estudiante13", "estudiante14", "estudiante15"], "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_30", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_30", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-14 22:47:59	2016-04-14 22:49:06	\N	1	0	60	F	120	0	0	1	2016-04-14 22:48:06	localhost.localdomain#3258
16	datos/maquinas	playbook	main	FAILED	playbook	df4d0278-dcd4-4927-b8f5-e29580af3838	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_5", "variables": ["root", "estudiante1", "estudiante2", "estudiante3", "estudiante4", "estudiante5", "estudiante6", "estudiante7", "estudiante8", "estudiante9", "estudiante10", "estudiante11", "estudiante12", "estudiante13", "estudiante14", "estudiante15"], "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_5", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_5", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 16:32:27	2016-04-15 16:33:38	\N	1	0	60	F	120	0	0	1	2016-04-15 16:32:38	localhost.localdomain#3938
15	datos/maquinas	playbook	main	FAILED	playbook	ac55a288-dc33-4a7c-b4db-36d6f05196cf	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_3", "variables": "root", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_3", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_3", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 16:12:02	2016-04-15 16:13:15	\N	1	0	60	F	120	0	0	1	2016-04-15 16:12:15	localhost.localdomain#3938
17	datos/maquinas	playbook	main	FAILED	playbook	f3208a7c-d0da-4424-9563-95c0f9c3002f	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_10", "variables": "{'somelist': ['root', 'estudiante1', 'estudiante2', 'estudiante3', 'estudiante4', 'estudiante5', 'estudiante6', 'estudiante7', 'estudiante8', 'estudiante9', 'estudiante10', 'estudiante11', 'estudiante12', 'estudiante13', 'estudiante14', 'estudiante15'], 'origen': FieldStorage('archivo', 'Archivo.txt', '')}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_10", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_10", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 17:26:29	2016-04-15 17:27:44	\N	1	0	60	F	120	0	0	1	2016-04-15 17:26:44	localhost.localdomain#3938
19	datos/maquinas	playbook	main	FAILED	playbook	eb8d403f-62ed-40be-a193-4e3d8002ace2	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_12", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': FieldStorage('archivo', 'Archivo.txt', '')}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_12", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_12", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 17:35:22	2016-04-15 17:36:37	\N	1	0	60	F	120	0	0	1	2016-04-15 17:35:37	localhost.localdomain#3938
18	datos/maquinas	playbook	main	FAILED	playbook	825f526b-2ec0-492b-8bd2-45d73d3f6eb6	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_11", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': FieldStorage('archivo', 'Archivo.txt', '')}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_11", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_11", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 17:30:58	2016-04-15 17:32:03	\N	1	0	60	F	120	0	0	1	2016-04-15 17:31:03	localhost.localdomain#3938
20	datos/maquinas	playbook	main	FAILED	playbook	52366045-e6e5-4758-8196-ff7174bc7d05	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_13", "variables": "origen=FieldStorage('archivo', 'Archivo.txt', '')somelist=['Carlos', 'centos']", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_13", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_13", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 17:58:49	2016-04-15 18:00:01	\N	1	0	60	F	120	0	0	1	2016-04-15 17:59:01	localhost.localdomain#3938
21	datos/maquinas	playbook	main	FAILED	playbook	01c8b480-e056-41b8-885b-6ff1985ab771	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_14", "variables": "origen=FieldStorage('archivo', 'Archivo.txt', '')somelist=['Carlos', 'centos']", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_14", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_14", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:02:20	2016-04-15 18:03:34	\N	1	0	60	F	120	0	0	1	2016-04-15 18:02:34	localhost.localdomain#3938
29	datos/maquinas	playbook	main	COMPLETED	playbook	5eb4eb05-8c77-4c6c-801b-5a5d371e4044	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_22", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': 'Archivo.txt'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_22", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_22", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 20:12:44	2016-04-15 20:13:52	\N	1	0	60	F	120	0	1	0	2016-04-15 20:12:52	localhost.localdomain#6218
27	datos/maquinas	playbook	main	COMPLETED	playbook	eabb28f7-ec2c-4719-8b7d-c7653b4ee2b1	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_20", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': 'Archivo.txt'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_20", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_20", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 19:28:03	2016-04-15 19:29:21	\N	1	0	60	F	120	0	1	0	2016-04-15 19:28:21	localhost.localdomain#6218
22	datos/maquinas	playbook	main	FAILED	playbook	219bb3a9-eed5-40ef-a11b-5dfb7f1cbbd3	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_15", "variables": "origen=somelist=['Carlos', 'centos']", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_15", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_15", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:23:33	2016-04-15 18:24:44	\N	1	0	60	F	120	0	0	1	2016-04-15 18:23:44	localhost.localdomain#6218
24	datos/maquinas	playbook	main	FAILED	playbook	3a6487fb-b741-48b3-8d48-cf836d6de9fb	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_17", "variables": "origen=somelist=['Carlos', 'centos']", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_17", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_17", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:36:13	2016-04-15 18:37:26	\N	1	0	60	F	120	0	0	1	2016-04-15 18:36:26	localhost.localdomain#6218
23	datos/maquinas	playbook	main	FAILED	playbook	b523fe8f-2924-4a6a-9fb2-18cf91b45911	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_16", "variables": "origen=somelist=['Carlos', 'centos']", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_16", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_16", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:34:57	2016-04-15 18:36:10	\N	1	0	60	F	120	0	0	1	2016-04-15 18:35:10	localhost.localdomain#6218
26	datos/maquinas	playbook	main	COMPLETED	playbook	4776c327-0ca8-4042-9f70-2ed9ecfeab95	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_19", "variables": "{'somelist': 'Carlos', 'origen': 'Archivo.txt'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_19", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_19", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:42:21	2016-04-15 18:43:33	\N	1	0	60	F	120	0	1	0	2016-04-15 18:42:33	localhost.localdomain#6218
25	datos/maquinas	playbook	main	FAILED	playbook	a02ff7ab-3d4d-49b2-bda0-ed0c53286f86	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_18", "variables": "Archivo.txt", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_18", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_18", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 18:37:32	2016-04-15 18:38:44	\N	1	0	60	F	120	0	0	1	2016-04-15 18:37:44	localhost.localdomain#6218
28	datos/maquinas	playbook	main	COMPLETED	playbook	c4b92394-65bd-4c2c-a8cf-7a9559dbdf07	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_21", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': 'Archivo.txt'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_21", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_21", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 19:28:50	2016-04-15 19:30:07	\N	1	0	60	F	120	0	1	0	2016-04-15 19:29:07	localhost.localdomain#6218
30	datos/maquinas	playbook	main	COMPLETED	playbook	46a8f8dc-ad12-4c70-9b8e-db52ad705f39	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_23", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': '/home/Carlos/Descargas/web2py/applications/datos/uploads/sabananotas.pdf'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_23", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_23", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 20:16:40	2016-04-15 20:17:56	\N	1	0	60	F	120	0	1	0	2016-04-15 20:16:56	localhost.localdomain#6218
31	datos/maquinas	playbook	main	COMPLETED	playbook	ced15e9f-4842-4701-91bd-3d5b0a849b6d	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_24", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': '/home/Carlos/Descargas/web2py/applications/datos/uploads/sabananotas.pdf'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_24", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_24", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 20:23:55	2016-04-15 20:25:05	\N	1	0	60	F	120	0	1	0	2016-04-15 20:24:05	localhost.localdomain#6218
32	datos/maquinas	playbook	main	COMPLETED	playbook	c83d639b-2e64-4b94-a98f-79e0b967d6d5	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/None_25", "variables": "{'somelist': ['Carlos', 'centos'], 'origen': '/home/Carlos/Descargas/web2py/applications/datos/uploads/Archivo.txt'}", "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/None_25", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/None_25", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/copiarArchivo.yml"}	T	2016-04-15 20:33:10	2016-04-15 20:34:14	\N	1	0	60	F	120	0	1	0	2016-04-15 20:33:14	localhost.localdomain#6218
33	datos/maquinas	playbook	main	QUEUED	playbook	a459df37-9db6-42d7-8a4a-9a5c48547017	["1", "2"]	{"nombre": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/resultados/1_36", "variables": null, "ruta_extra": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/variables/1_36", "hosts": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/1_36", "playbook": "/home/Carlos/Descargas/web2py/applications/datos/private/Ansible/Playbooks/reiniciar.yml"}	T	2016-04-21 14:18:47	2016-04-21 14:18:47	\N	1	0	60	F	120	0	0	0	\N	
\.


--
-- Data for Name: scheduler_task_deps; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY scheduler_task_deps (id, job_name, task_parent, task_child, can_visit) FROM stdin;
\.


--
-- Name: scheduler_task_deps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('scheduler_task_deps_id_seq', 1, false);


--
-- Name: scheduler_task_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('scheduler_task_id_seq', 33, true);


--
-- Data for Name: scheduler_worker; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY scheduler_worker (id, worker_name, first_heartbeat, last_heartbeat, status, is_ticker, group_names, worker_stats) FROM stdin;
10	localhost.localdomain#6218	2016-04-15 18:16:33	2016-04-15 20:46:04	ACTIVE	T	|main|	{"status": "ACTIVE", "errors": 0, "workers": 1, "queue": 0, "empty_runs": 253, "sleep": 3, "distribution": {"main": {"workers": [{"c": 0, "name": "localhost.localdomain#6218"}]}}, "total": 11}
\.


--
-- Name: scheduler_worker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('scheduler_worker_id_seq', 10, true);


--
-- Data for Name: student_x_machine; Type: TABLE DATA; Schema: public; Owner: udistrital
--

COPY student_x_machine (id, ip_machine, code_student, name_student, semester, is_active, created_on, created_by, modified_on, modified_by) FROM stdin;
1	4	20101020094	Estudiante Camilo	2016-I	T	2016-04-26 12:17:28	11	2016-04-26 12:17:28	11
2	1	20092001015	Estudiante Carlos	2016-I	T	2016-04-26 12:19:09	11	2016-04-26 12:19:09	11
\.


--
-- Name: student_x_machine_id_seq; Type: SEQUENCE SET; Schema: public; Owner: udistrital
--

SELECT pg_catalog.setval('student_x_machine_id_seq', 2, true);


--
-- Name: auth_cas_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_cas
    ADD CONSTRAINT auth_cas_pkey PRIMARY KEY (id);


--
-- Name: auth_event_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_event
    ADD CONSTRAINT auth_event_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_membership_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_membership
    ADD CONSTRAINT auth_membership_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: course_group_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY course_group
    ADD CONSTRAINT course_group_pkey PRIMARY KEY (id);


--
-- Name: course_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_pkey PRIMARY KEY (id);


--
-- Name: job_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY job
    ADD CONSTRAINT job_pkey PRIMARY KEY (id);


--
-- Name: machine_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY machine
    ADD CONSTRAINT machine_pkey PRIMARY KEY (id);


--
-- Name: port_machine_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY port_machine
    ADD CONSTRAINT port_machine_pkey PRIMARY KEY (id);


--
-- Name: scheduler_run_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_run
    ADD CONSTRAINT scheduler_run_pkey PRIMARY KEY (id);


--
-- Name: scheduler_task_deps_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_task_deps
    ADD CONSTRAINT scheduler_task_deps_pkey PRIMARY KEY (id);


--
-- Name: scheduler_task_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_task
    ADD CONSTRAINT scheduler_task_pkey PRIMARY KEY (id);


--
-- Name: scheduler_task_uuid_key; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_task
    ADD CONSTRAINT scheduler_task_uuid_key UNIQUE (uuid);


--
-- Name: scheduler_worker_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_worker
    ADD CONSTRAINT scheduler_worker_pkey PRIMARY KEY (id);


--
-- Name: scheduler_worker_worker_name_key; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY scheduler_worker
    ADD CONSTRAINT scheduler_worker_worker_name_key UNIQUE (worker_name);


--
-- Name: student_x_machine_pkey; Type: CONSTRAINT; Schema: public; Owner: udistrital; Tablespace: 
--

ALTER TABLE ONLY student_x_machine
    ADD CONSTRAINT student_x_machine_pkey PRIMARY KEY (id);


--
-- Name: auth_cas_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_cas
    ADD CONSTRAINT auth_cas_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_event_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_event
    ADD CONSTRAINT auth_event_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_membership_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_membership
    ADD CONSTRAINT auth_membership_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) ON DELETE CASCADE;


--
-- Name: auth_membership_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_membership
    ADD CONSTRAINT auth_membership_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: auth_permission_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_group_id_fkey FOREIGN KEY (group_id) REFERENCES auth_group(id) ON DELETE CASCADE;


--
-- Name: course_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_created_by_fkey FOREIGN KEY (created_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: course_group_cod_course_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course_group
    ADD CONSTRAINT course_group_cod_course_fkey FOREIGN KEY (cod_course) REFERENCES course(id) ON DELETE CASCADE;


--
-- Name: course_group_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course_group
    ADD CONSTRAINT course_group_created_by_fkey FOREIGN KEY (created_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: course_group_id_teacher_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course_group
    ADD CONSTRAINT course_group_id_teacher_fkey FOREIGN KEY (id_teacher) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: course_group_modified_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course_group
    ADD CONSTRAINT course_group_modified_by_fkey FOREIGN KEY (modified_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: course_modified_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY course
    ADD CONSTRAINT course_modified_by_fkey FOREIGN KEY (modified_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: job_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY job
    ADD CONSTRAINT job_user_id_fkey FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: machine_code_course_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY machine
    ADD CONSTRAINT machine_code_course_fkey FOREIGN KEY (code_course) REFERENCES course(id) ON DELETE CASCADE;


--
-- Name: machine_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY machine
    ADD CONSTRAINT machine_created_by_fkey FOREIGN KEY (created_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: machine_modified_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY machine
    ADD CONSTRAINT machine_modified_by_fkey FOREIGN KEY (modified_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: port_machine_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY port_machine
    ADD CONSTRAINT port_machine_created_by_fkey FOREIGN KEY (created_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: port_machine_ip_machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY port_machine
    ADD CONSTRAINT port_machine_ip_machine_fkey FOREIGN KEY (ip_machine) REFERENCES machine(id) ON DELETE CASCADE;


--
-- Name: port_machine_modified_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY port_machine
    ADD CONSTRAINT port_machine_modified_by_fkey FOREIGN KEY (modified_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: scheduler_run_task_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_run
    ADD CONSTRAINT scheduler_run_task_id_fkey FOREIGN KEY (task_id) REFERENCES scheduler_task(id) ON DELETE CASCADE;


--
-- Name: scheduler_task_deps_task_child_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY scheduler_task_deps
    ADD CONSTRAINT scheduler_task_deps_task_child_fkey FOREIGN KEY (task_child) REFERENCES scheduler_task(id) ON DELETE CASCADE;


--
-- Name: student_x_machine_created_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY student_x_machine
    ADD CONSTRAINT student_x_machine_created_by_fkey FOREIGN KEY (created_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: student_x_machine_ip_machine_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY student_x_machine
    ADD CONSTRAINT student_x_machine_ip_machine_fkey FOREIGN KEY (ip_machine) REFERENCES port_machine(id) ON DELETE CASCADE;


--
-- Name: student_x_machine_modified_by_fkey; Type: FK CONSTRAINT; Schema: public; Owner: udistrital
--

ALTER TABLE ONLY student_x_machine
    ADD CONSTRAINT student_x_machine_modified_by_fkey FOREIGN KEY (modified_by) REFERENCES auth_user(id) ON DELETE CASCADE;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

