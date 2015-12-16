/**
 * Created by longlan on 2015/12/16.
 */
$('#likes').click(function(){
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/ran/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});