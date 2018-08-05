//JavaScript代码区域
layui.use(['element','form'], function(){
  var $ = layui.jquery,
  form = layui.form;

  now_hash = location.hash


  if (now_hash!="" && $("[class='layui-this']")){             //回到首页时刷新页面
        window.location.href ="/home";
   }
  window.addEventListener('hashchange', function(){    //hash 改变进行页面展示
        var hash = location.hash;
        hash = hash.split("#")[1];
        $(".layui-body").load("static/model/"+hash+"/"+hash+".html",function(responseTxt,statusTxt,xhr){
                if(statusTxt=="success"){
                    if($("link[href*="+hash+"]").length == 0 ){
                          $('head').append('<link rel="stylesheet" href=/static/model/'+hash+"/"+hash+'.css>');//加载css
                    };
                    $.getScript('/static/model/'+hash+"/"+hash+'.js');   //加载js/加载css
                    form.render();  //表单进行渲染
                }
                if(statusTxt=="error"){
                    window.location.href ="/404.html"   //加载失败时返回404页面
                }
                });
        });

});