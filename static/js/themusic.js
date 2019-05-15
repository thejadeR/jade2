$(function () {


var $p = 0
$('.todel').click(function () {
    $p = $(this).prev()
    // console.log($p)
})



    $('.tijiao').click(function () {

        $.ajax({
            url:'/queren/',
            type:'get',
            data:{'passwd':$('#passwd').val()},
            success:function (recv) {

                var msg = recv.msg
                if (parseInt(msg))
                {
                    console.log('密碼正確')
                    // console.log($($p).attr('data-id'))
                    $.ajax({
                        url: '/del_music/',
                        type: 'get',
                        data: {'dz_id': $p.attr('data-id')},
                        success:function (recv2) {
                            var msg2 = recv2.msg

                            if (parseInt(msg2)){
                                 $('#mengban2').hide()

                            }else {
                                $('.tips').html('刪除失敗')
                            }
                        }

                    })
                }
                else {

                    $('.tips').html('管理员密码不正确')
                }


                }


        })





    })






})