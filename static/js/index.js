//JavaScript代码区域
layui.use(['element','carousel','layer','form'], function(){
  var $ = layui.jquery,
  element = layui.element,
  layer = layui.layer,
  form = layui.form,
  carousel  = layui.carousel;

  var login_hash = 'login'        //定义登录hash
  var home_hash = 'home'         //定义后台管理hash
  var index = 'index'             //定义主页

  carousel.render({
    elem: '#'+index
    ,width: '100%' //设置容器宽度
    ,arrow: 'always' //始终显示箭头
    ,anim: 'fade' //切换动画方式
    ,height:'100vh'
   });

   $(login_hash).hide();        //登录模块默认隐藏
   window.addEventListener('hashchange', function(){
        var hash=location.hash.replace('#','');
        if (hash==login_hash){
//            old_hash='.'+hash;   //classd登录
            $('#'+index).hide();
            $("."+hash).show();
        }else if (hash==home_hash){
            $("."+hash).hide();
        }

    });

   function myFunction(){
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
                   if (data["code"]===1){
                        window.location.href ="http://127.0.0.1:5000/home";
                   }else if (data["code"]===2){
                        layer.msg("密码错误");
                   }else if(data["code"]===3){
                         layer.msg("账户不存在");
                   }else{
                        layer.msg("系统异常");
                   };
            });
        };
     });
});