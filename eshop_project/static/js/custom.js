// console.log('this is custom js')

function sendArticleComment(){
    // console.log('submit article comment')
    const comment = $('#commentText').val();
    // console.log(comment)

    $.get('/articles/add-article-comment', {
        articleComment: comment,
        articleId: 23,
        parentId: null,
    }).then(res => {
        console.log(res)
    });

}