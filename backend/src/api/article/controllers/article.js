'use strict';

/**
 *  article controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::article.article', ({strapi}) => ({
    async customArticleAction(ctx) {
        try {
            ctx.body = `ok, hello world`;
        } catch(err) {
            ctx.body = err;
        }
    },
    async find(ctx) {
        ctx.query = {...ctx.query, local: 'en' }

        const { data, meta } = await super.find(ctx);

        meta.date = Date.now()

        return { data, meta }
    },
    // customized lines - does same thing as findOne() but manually
    // async findOne(ctx) {
    //     const { id } = ctx.params;
    //     const { query } = ctx;

    //     const entity = await strapi.service('api::article.article').findOne(id, query);
    //     const sanitizedEntity = await this.sanitizeOutput(entity,ctx);

    //     return this.transformResponse(sanitizedEntity);
    // }
}));
