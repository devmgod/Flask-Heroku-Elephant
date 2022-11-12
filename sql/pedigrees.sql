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

 Date: 12/11/2022 00:01:42
*/


-- ----------------------------
-- Table structure for pedigrees
-- ----------------------------
DROP TABLE IF EXISTS "public"."pedigrees";
CREATE TABLE "public"."pedigrees" (
  "id" int4 NOT NULL DEFAULT nextval('pedigrees_id_seq'::regclass),
  "title" varchar(50) COLLATE "pg_catalog"."default",
  "description" varchar(1000) COLLATE "pg_catalog"."default",
  "media" varchar(150) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Records of pedigrees
-- ----------------------------
INSERT INTO "public"."pedigrees" VALUES (1, 'Allentown', 'Purchased by Jim Payette and Stephen Fishler in 1987, the Allentowns only numbered 135 comics, but contained some of the highest cgc_graded copies of several key issues such as Detective Comics #27, Marvel Comics #1, Captain America #1 and Batman #1. The original owner had discovered his mother had saved his small collection when he found them in her closet. His acquaintance, a local antique dealer contacted six comic book dealers to place bids, with Payette and Fishler bidding the highest. Even though the comics do not exhibit any distinctive markings, nearly every copy has retained its provenance.', '../static/images/pedigrees/allentown.jpg');

-- ----------------------------
-- Primary Key structure for table pedigrees
-- ----------------------------
ALTER TABLE "public"."pedigrees" ADD CONSTRAINT "pedigrees_pkey" PRIMARY KEY ("id");
