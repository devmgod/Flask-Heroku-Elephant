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

 Date: 12/11/2022 00:01:10
*/


-- ----------------------------
-- Table structure for comics_offers
-- ----------------------------
DROP TABLE IF EXISTS "public"."comics_offers";
CREATE TABLE "public"."comics_offers" (
  "id" int4 NOT NULL DEFAULT nextval('comics_offers_id_seq'::regclass),
  "offer_id" int4,
  "comic_id" int4
)
;

-- ----------------------------
-- Records of comics_offers
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table comics_offers
-- ----------------------------
ALTER TABLE "public"."comics_offers" ADD CONSTRAINT "comics_offers_pkey" PRIMARY KEY ("id");
