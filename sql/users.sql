/*
 Navicat Premium Data Transfer

 Source Server         : postgres
 Source Server Type    : PostgreSQL
 Source Server Version : 140005
 Source Host           : localhost:5432
 Source Catalog        : comicswap2
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 140005
 File Encoding         : 65001

 Date: 12/11/2022 00:01:50
*/


-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS "public"."users";
CREATE TABLE "public"."users" (
  "id" int4 NOT NULL DEFAULT nextval('users_id_seq'::regclass),
  "username" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "fname" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "lname" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "email" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "password" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "confirmation_token" varchar(50) COLLATE "pg_catalog"."default",
  "confirmed" bool,
  "blocked" bool,
  "mailinglist" bool,
  "role" int4 NOT NULL
)
;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO "public"."users" VALUES (1, 'magiclar', 'Larry', 'Volz', 'imaginologist@gmail.com', 'testPassword1', 'OU812', 'f', 'f', 't', 0);
INSERT INTO "public"."users" VALUES (2, 'comicrodney', 'Rodney', 'Chakan', 'something@thecomicswap.com', 'testPassword2', 'ASDF1234', 'f', 'f', 't', 1);

-- ----------------------------
-- Uniques structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_username_key" UNIQUE ("username");
ALTER TABLE "public"."users" ADD CONSTRAINT "users_email_key" UNIQUE ("email");
ALTER TABLE "public"."users" ADD CONSTRAINT "users_password_key" UNIQUE ("password");

-- ----------------------------
-- Primary Key structure for table users
-- ----------------------------
ALTER TABLE "public"."users" ADD CONSTRAINT "users_pkey" PRIMARY KEY ("id");
