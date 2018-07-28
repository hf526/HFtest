//JavaScript代码区域
layui.use(['element','carousel','layer'], function(){
  var $ = layui.jquery,
  element = layui.element,
  layer = layui.layer,
  carousel  = layui.carousel;
  carousel.render({
    elem: '#carousel'
    ,width: '100%' //设置容器宽度
    ,arrow: 'always' //始终显示箭头
    ,anim: 'fade' //切换动画方式
    ,height:'100vh'
   });

   var old_hash='login'
   window.addEventListener('hashchange', function(){
        $(old_hash).hide();
        var hash=location.hash.replace('#','');
//        var change="[href='"+hash+"']"
//        alert(change)
//        $(change)
        old_hash='.'+hash;
        $('#carousel').hide();
        $("."+hash).show();
    })

});