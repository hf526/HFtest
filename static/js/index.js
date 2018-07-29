//JavaScript代码区域
layui.use(['element','carousel','layer','form'], function(){
  var $ = layui.jquery,
  element = layui.element,
  layer = layui.layer,
  form = layui.form,
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
        old_hash='.'+hash;
        $('#carousel').hide();
        $("."+hash).show();
    });

   function myFunction(){
            alert('sss');
           window.location.hash = "";
//         window.location = "http://127.0.0.1:5000/";
////         window.location = "http://www.52lefeng.club/";
    };
    $("#login").click(function(){
        username=$('[name=username]').val();
        password=$('[name=password]').val();
        if (username=='' || password==''){
              layer.msg("账号/密码不能为空");
        }else{
            $.post("/login",
                {
                    username:username,
                    password:password
                },
                function(data,status){
                   if (data["type"]===1){
                        alert("数据: \n" + JSON.stringify(data) + "\n状态: " + status);
                   }else if (data["type"]===2){
                        layer.msg("密码错误");
                   }else if(data["type"]===3){
                         layer.msg("账户不存在");
                   }else{
                        layer.msg("系统异常");
                   };
            });
        };
     });
});