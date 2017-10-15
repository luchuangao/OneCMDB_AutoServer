/**
 * Created by Administrator on 2017/10/15.
 */

(function (jq) {
    var GLOBAL_DICT = {};
    // 为字符串创建format方法，用于字符串格式化
    String.prototype.format = function (args) {
        return this.replace(/\{(\w+)\}/g, function (s, i) {
            return args[i];
        });
    };

    function initail(url) {
        $.ajax({
            url: url,
            type: 'GET', //获取数据
            dataType: 'JSON',
            success: function (arg) {
                /*
                 {
                 'server_list':list(server_list), # 所有数据
                 'table_config':table_config      # 所有配置
                 }
                 */
                $.each(arg.global_dict, function (k, v) {
                    GLOBAL_DICT[k] = v
                });
                initTableHeader(arg.table_config);
                initTableBody(arg.server_list, arg.table_config);
            }
        })
    }

    function initTableHeader(tableConfig) {
        /*
         [
         {'q':'id','title':'ID'},
         {'q':'hostname','title':'主机名'},
         ]
         */
        $.each(tableConfig, function (k, v) {
            if (v.display){
                var tag = document.createElement('th');
                tag.innerHTML = v.title;
                $('#tbHead').find('tr').append(tag);
            }
        })
    }

    function initTableBody(serverList, tableConfig) {

        /*
         serverList = [
         {'id': 1, 'hostname':c2.com, create_at: xxxx-xx-xx-},
         {'id': 1, 'hostname':c2.com, create_at: xxxx-xx-xx-},
         {'id': 1, 'hostname':c2.com, create_at: xxxx-xx-xx-},
         {'id': 1, 'hostname':c2.com, create_at: xxxx-xx-xx-},
         ]
         */
        $.each(serverList, function (k, row) {
            // row: {'id': 1, 'hostname':c2.com, create_at: xxxx-xx-xx-}
            /*
             <tr>
             <td>id</td>
             <td>hostn</td>
             <td>create</td>
             </tr>
             */
            var tr = document.createElement('tr')
            $.each(tableConfig, function (kk, rrow) {
                // kk: 1  rrow:{'q':'id','title':'ID'},         // rrow.q = "id"
                // kk: .  rrow:{'q':'hostname','title':'主机名'},// rrow.q = "hostname"
                // kk: .  rrow:{'q':'create_at','title':'创建时间'}, // rrow.q = "create_at"
                if (rrow.display) {
                    var td = document.createElement('td');
                    var newKwargs = {}; // {'n1':'1','n2':'123'}
                    $.each(rrow.text.kwargs, function (kkk, vvv) {
                        var av = vvv;
                        if (vvv.substring(0, 2) == '@@') {
                            var global_dict_key = vvv.substring(2, vvv.length);
                            var nid = row[rrow.q];
                            console.log(nid, global_dict_key);
                            $.each(GLOBAL_DICT[global_dict_key], function (gk, gv) {
                                if (gv[0] == nid) {
                                    av = gv[1];
                                }
                            })
                        }
                        if (vvv[0] == '@') {
                            av = row[vvv.substring(1, vvv.length)];
                        }
                        newKwargs[kkk] = av;
                    });
                    var newText = rrow.text.tpl.format(newKwargs);
                    td.innerHTML = newText;
                    $(tr).append(td);
                }

            });
            $('#tbBody').append(tr);
        })
    }

    jq.extend({
        xx: function (url) {
            initail(url);
        }
    })
})(jQuery);