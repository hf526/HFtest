//JavaScript代码区域
layui.use(['table'], function(){
  var $ = layui.jquery,
  table = layui.table,
  form = layui.form;

//项目列表需要的元素
    var project_list = ".project_list"; //项目列表
    var add_project = ".add_project" ;  //添加项目
    var select_btn = '.project_list button';
    var new_btn = '.new';   //新增项目按钮
    var select_input = ".project_list input";
    var add_input = ".add_project input"
    var input = {};

//新增项目时需要的元素
    var save_btn = '.layui-input-block button:nth-child(1)' ; //保存按钮
    var cancel_btn = '.layui-input-block button:nth-child(2)'; //取消按钮

    table.render({
        elem: '#demo'
        ,height: 315
        ,url: '/home/projectlist' //数据接口
        ,page: true //开启分页
        ,cols: [[ //表头
          {field: 'id', title: 'ID', width:80, sort: true, fixed: 'left'}
          ,{field: 'username', title: '用户名', width:80}
          ,{field: 'sex', title: '性别', width:80}
          ,{field: 'city', title: '城市', width:80}
          ,{field: 'sign', title: '签名', width: 177}
          ,{field: 'experience', title: '积分', width: 80, sort: true}
          ,{field: 'score', title: '评分', width: 80, sort: true}
          ,{field: 'classify', title: '职业', width: 80}
          ,{field: 'wealth', title: '财富', width: 135, sort: true}
        ]]
    });
    $(select_btn).click(function(){          //查询项目列表
         input = {}
         for(var i=0;i<$(select_input).length;i++){
                input[$(select_input)[i].getAttribute('name')] = $(select_input)[i].value;
            }
             $.ajax({
                type: "POST",
                url: "/home/project/selectproject",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(input),
                dataType: "json",
                success: function (message) {
                    if (message > 0) {
                        alert("查询成功");
                    }
                },
                error: function (message) {
                    alert("查询失败");
                }
            });
    });

    $(new_btn).click(function(){              //新增项目操作
        $(new_btn).hide();
        $(project_list).hide();
        $(add_project).show();
    });

    $(save_btn).click(function(){      //保存项目提交ajax
        if ($(add_input)[0].value ==""){
                layer.msg("项目名不能为空");
        }else{
                input = {}
                for(var i=0;i<$(add_input).length;i++){
                    var val = $(add_input)[i].value.replace(/[ ]/g,"")
                    val = val.replace(/\ +/g,"")
                    input[$(add_input)[i].getAttribute('name')] = val;
                    }
                 $.post("/home/saveproject",
                    JSON.stringify(input),
                        function(data,status){
                            $(new_btn).show();
                            $(project_list).show();
                            $(add_project).hide();
                            form.render();
                    }
                    ,"json");
        }
    });

    $(cancel_btn).click(function(){    //取消操作
        $(new_btn).show();
        $(project_list).show();
        $(add_project).hide();
        form.render();
    });

});