//JavaScript代码区域
layui.use(['element','carousel','layer','form'], function(){
  var $ = layui.jquery,
  element = layui.element,
  layer = layui.layer,
  form = layui.form,
  carousel  = layui.carousel;

  var login = '.index_from'        //设置登录模块class  变量
  var home_hash = 'home'         //定义后台管理
  var col = '.layui-carousel'             //设置轮播图class  变量
  var hash = location.hash    //获取当前hash地址

   carousel.render({
    elem: col
    ,width: '100%' //设置容器宽度
    ,arrow: 'always' //始终显示箭头
    ,anim: 'fade' //切换动画方式
    ,height:'100vh'
   });

   $(login).hide();        //登录模块默认隐藏

   window.addEventListener('hashchange', function(){    //hash 改变进行页面展示
            $(col).hide();
            $(login).show();
    });

   if (hash!="" && $(login).hide()){             //回到首页时刷新页面
        window.location.href ="http://127.0.0.1:5000"
   }

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
                        window.location.href ="/home";
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