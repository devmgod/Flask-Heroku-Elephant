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

 Date: 12/11/2022 00:00:08
*/


-- ----------------------------
-- Table structure for comics
-- ----------------------------
DROP TABLE IF EXISTS "public"."comics";
CREATE TABLE "public"."comics" (
  "id" int4 NOT NULL DEFAULT nextval('comics_id_seq'::regclass),
  "owner_id" int4 NOT NULL,
  "title" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "issue_num" int4 NOT NULL,
  "cgc_grade" float8,
  "assessed_value" float8,
  "assessed_source" varchar(50) COLLATE "pg_catalog"."default",
  "thumbnail" text COLLATE "pg_catalog"."default",
  "cover_pic" text COLLATE "pg_catalog"."default",
  "back_cover_pic" text COLLATE "pg_catalog"."default",
  "extra_media" text COLLATE "pg_catalog"."default",
  "publisher" text COLLATE "pg_catalog"."default",
  "month" varchar(10) COLLATE "pg_catalog"."default",
  "year" int4,
  "notes" text COLLATE "pg_catalog"."default",
  "signed" bool,
  "pedigree" int4,
  "location" int4
)
;

-- ----------------------------
-- Records of comics
-- ----------------------------
INSERT INTO "public"."comics" VALUES (1, 1, 'Batman', 265, 9.6, 40, 'CGC', '../static/images/batman-p-500.jpg', '../static/images/batman-p-1080.jpg', '', '', 'DC', NULL, 1975, 'Title is Batman''s greatest failure', 't', 1, 0);
INSERT INTO "public"."comics" VALUES (2, 1, 'Captain America', 100, 9.9, 5400, 'CGC', '../static/images/captain_america-p-250.jpg', '../static/images/captain_america-p-1080.jpg', '', '', 'Marvel', NULL, 1968, 'Title is ''Big Premier Issue''', 'f', 2, 0);
INSERT INTO "public"."comics" VALUES (3, 1, 'Doctor Strange', 50, 9.9, 9.99, 'CGC', '../static/images/Dr_strange-p-250.jpg', '../static/images/Dr_strange-p-100.jpg', '', '', 'Marvel', NULL, 1993, 'Holographic giant issue Guest starring Ghost Rider, Hulk and Silver Surfer''', 'f', 3, 0);
INSERT INTO "public"."comics" VALUES (4, 2, 'Fantastic 4', 52, 9.9, 4000, 'CGC', '../static/images/fantastic4_and_black_panther-p-250.jpg', '../static/images/fantastic4_and_black_panther-p-1080.jpg', '', '', 'Marvel', 'July', 1966, 'Featuring Black Panther', 'f', 4, 0);
INSERT INTO "public"."comics" VALUES (5, 2, 'Amazing Fantasy Featuring Spider-Man', 15, 9, 1100000, 'CGC', '../static/images/spider_man_coolest_pic-p-250.jpg', '../static/images/spider_man_coolest_pic.jpg', '', '', 'Marvel', 'August', 1962, 'First appearance of Spider-Man', 'f', 5, 0);
INSERT INTO "public"."comics" VALUES (6, 2, 'Action Comics featuring Superman', 419, 9, 6, 'CGC', '../static/images/superman-p-250.jpg', '../static/images/superman-p-1080.jpg', '', '', 'Marvel', 'August', 1972, 'First appearance of Spider-Man', 'f', 5, 0);

-- ----------------------------
-- Primary Key structure for table comics
-- ----------------------------
ALTER TABLE "public"."comics" ADD CONSTRAINT "comics_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Foreign Keys structure for table comics
-- ----------------------------
ALTER TABLE "public"."comics" ADD CONSTRAINT "comics_owner_id_fkey" FOREIGN KEY ("owner_id") REFERENCES "public"."users" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION;
