$(function () {
  // console.log('enter index.js')
//
//
// $('.themusic').click(function () {
//     console.log('點擊')

//     $('.ms_title').html($(this).find('p').first().attr('data-title'))
//
//     $('.the_audio').empty()
//     $('<audio controls><source src="/static/upload/index/' + $(this).find('p').first().attr('data-src') + ' " type="audio/mpeg" class="ms_src"> 您的浏览器不支持 audio 元素。</audio>').appendTo('.the_audio')
//
//
// })

    // /
    // // 获取 typeIndex
    // var typeIndex = $.cookie('typeIndex')
    // if (typeIndex){ // 有下标记录
    //     // 根据下标获取对应li，并添加上'active'
    //     $('#foot2 li').eq(typeIndex).addClass('foot_active')
    // } else {    // 没有下标记录
    //     // 默认就是第一个
    //     $('#foot2 li:first').addClass('foot_active')
    // }
    //


$('.themusic').click(function () {
    console.log('點擊')

    $('.ms_title').html($(this).attr('data-title'))

    $('.the_audio').empty()
    $('<audio controls><source src="/static/upload/index/' + $(this).attr('data-src') + ' " type="audio/mpeg" class="ms_src"> 您的浏览器不支持 audio 元素。</audio>').appendTo('.the_audio')


})

    // 获取 typeIndex
    var typeIndex = $.cookie('typeIndex')
    if (typeIndex){ // 有下标记录
        // 根据下标获取对应li，并添加上'active'
        $('#foot2 li').eq(typeIndex).addClass('foot_active')
    } else {    // 没有下标记录
        // 默认就是第一个
        $('#foot2 li:first').addClass('foot_active')
    }


    // 侧边栏 分类 点击
    // 问题描述: 当点击分类时，样式添加成功，之后又会消失
    // 问题分析: 点击分类是 a标签，在样式设置完成后，会重新刷新页面；重新刷新页面，样式会被重置
    // 问题解决: 记录点击分类的下标

    // 用什么记录？  cookie
    // 为了方便操作cookie，引入 jquery.cookie.js
    // 设置cookie    $.cookie(key, value, opthions)
    // 获取cookie    $.cookie(key)
    // 删除cookie    $.cookie(key, null)
    // opthions选项  {'expires': 过期时间, path: 路径}
    $('#foot2 li').click(function () {
        // $(this) 被点击的 li
        // $(this).addClass('active')

        // 记录 分类 下标    $(this).index()
        $.cookie('typeIndex', $(this).index(), {expires: 3, path: '/'})
    })






    $('.thebt').click(function () {

        $('#mengban').show()

    })


    $('#tocancel').click(function () {

        $('#mengban').hide()

    })



    $('.todel').click(function () {

        $('#mengban2').show()

    })


    $('#tocancel2').click(function () {


        $('#mengban2').hide()
    })


})