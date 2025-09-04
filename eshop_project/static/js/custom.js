// console.log('this is custom js')

function sendArticleComment(articleId){
    // console.log('submit article comment')
    const comment = $('#commentText').val();
    // console.log(comment)
    const parentId = $('#parent_id').val();

    $.get('/articles/add-article-comment', {
        article_comment: comment,
        article_id: articleId,
        parent_id: parentId,
    }).then(res => {
        console.log(res);
        location.reload();
    });
}

function fillParentId(parentId){
    $('#parent_id').val(parentId);
    // window.scrollTo({top:2500, behavior:'smooth'});
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
}