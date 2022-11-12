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

 Date: 12/11/2022 00:01:27
*/


-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS "public"."messages";
CREATE TABLE "public"."messages" (
  "id" int4 NOT NULL DEFAULT nextval('messages_id_seq'::regclass),
  "maildate" timestamp(6) NOT NULL,
  "to_id" int4 NOT NULL,
  "from_id" int4 NOT NULL,
  "subject" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "content" text COLLATE "pg_catalog"."default" NOT NULL,
  "read" bool,
  "attachments" text COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of messages
-- ----------------------------
INSERT INTO "public"."messages" VALUES (1, '2022-11-11 13:30:04.232886', 1, 2, 'first db test of msgs', 'this would be a great place for some lorem ipsum.  But I''ll just type up some random content instead.  Okay, that should be enough.', 'f', '{''http://www.test.com'', ''http://www.test2.com''}');
INSERT INTO "public"."messages" VALUES (2, '2022-11-11 13:30:04.232886', 2, 1, 'NOT FOR USER #1 - 2nd db test of msgs', 'MORE TEXT!!!  this would be a great place for some lorem ipsum.  But I''ll just type up some random content instead.  Okay, that should be enough.', 'f', '{''http://www.test.com'', ''http://www.test2.com''}');
INSERT INTO "public"."messages" VALUES (3, '2022-11-11 13:30:04.232886', 1, 2, '2nd msg for user 1', 'this would be a great place for some lorem ipsum.  But I''ll just type up some random content instead.  Okay, that should be enough.', 'f', '{''http://www.test.com'', ''http://www.test2.com''}');
INSERT INTO "public"."messages" VALUES (4, '2022-11-11 13:32:44.951728', 2, 1, 'Re: asdf', 'asdf', 'f', '');

-- ----------------------------
-- Primary Key structure for table messages
-- ----------------------------
ALTER TABLE "public"."messages" ADD CONSTRAINT "messages_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table messages
-- ----------------------------
ALTER TABLE "public"."messages" ADD CONSTRAINT "messages_from_id_fkey" FOREIGN KEY ("from_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
