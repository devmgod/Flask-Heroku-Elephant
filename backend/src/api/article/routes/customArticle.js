module.exports = {
    routes: [
        {
            method: 'GET',
            path: '/customArticle',
            handler: 'article.customArticleAction',
            config: {
                auth: false,
            }
        }
    ]
}