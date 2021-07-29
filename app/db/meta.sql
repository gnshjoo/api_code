DROP TABLE IF EXISTS "public"."code";
CREATE SEQUENCE IF NOT EXISTS code_id_seq;
CREATE TABLE "public"."code" (
    "id" int4 NOT NULL DEFAULT nextval('code_id_seq'::regclass),
    "phone" varchar NOT NULL,
    "code" int8 NOT NULL,
    "created_date" timestamp NOT NULL DEFAULT now(),
    "type" varchar NOT NULL,
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."users";
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE "public"."users" (
    "id" int4 NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    "email" varchar(200),
    "password" varchar(200),
    "nickname" varchar(200),
    "name" varchar(200),
    "phone" varchar(200),
    "created_date" timestamp DEFAULT now(),
    "activate" bool DEFAULT false,
    PRIMARY KEY ("id")
);
