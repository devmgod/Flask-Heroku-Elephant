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

 Date: 12/11/2022 00:01:34
*/


-- ----------------------------
-- Table structure for offers
-- ----------------------------
DROP TABLE IF EXISTS "public"."offers";
CREATE TABLE "public"."offers" (
  "id" int4 NOT NULL DEFAULT nextval('offers_id_seq'::regclass),
  "title" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "num_comics_offered" int4,
  "user_offering" int4,
  "user_owner" int4,
  "owner_response" int4,
  "deal_id" int4,
  "payment_offer" float8,
  "additional_terms" varchar(150) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of offers
-- ----------------------------
INSERT INTO "public"."offers" VALUES (1, 'Fantastic 4 for your Batman', 1, 2, 1, 0, 0, 0, 'Contingent on pedigree being confirmed.');
INSERT INTO "public"."offers" VALUES (2, 'Captain America for your Amazing Spiderman', 1, 1, 2, 0, 0, 0, 'Looking forward to the deal.');
INSERT INTO "public"."offers" VALUES (3, 'Superman for your Doctor Strange', 1, 2, 1, 0, 0, 0, 'Assuming it''s not cursed by an evil trans-dimensional demon.');

-- ----------------------------
-- Primary Key structure for table offers
-- ----------------------------
ALTER TABLE "public"."offers" ADD CONSTRAINT "offers_pkey" PRIMARY KEY ("id");
