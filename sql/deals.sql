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

 Date: 12/11/2022 00:01:20
*/


-- ----------------------------
-- Table structure for deals
-- ----------------------------
DROP TABLE IF EXISTS "public"."deals";
CREATE TABLE "public"."deals" (
  "id" int4 NOT NULL DEFAULT nextval('deals_id_seq'::regclass),
  "date_of_agreement" date NOT NULL,
  "amt_owed_seller" float8,
  "amt_paid_to_seller" float8,
  "amt_owed_comicswap" float8,
  "amt_paid_comicswap" float8,
  "date_paid" date,
  "payment_status" float8,
  "offer_id" int4,
  "delivery_status" int4,
  "comic_condition" int4
)
;

-- ----------------------------
-- Records of deals
-- ----------------------------
INSERT INTO "public"."deals" VALUES (1, '2022-11-10', 0, 0, 12.5, 0, NULL, 0, 1, 0, 0);

-- ----------------------------
-- Primary Key structure for table deals
-- ----------------------------
ALTER TABLE "public"."deals" ADD CONSTRAINT "deals_pkey" PRIMARY KEY ("id");
