$(function(){
    $(window).scroll(function() {
        if($(this).scrollTop() >= 202) {
            $('.navbar').addClass('navbar-fixed-top');
        }
        else{
            $('.navbar').removeClass('navbar-fixed-top');
        }
    });
});

$('.report-form').submit(function (e) {
        var name = val = $('#InputName').val();
        var mail = val = $('#InputEmail1').val();
        var massage = val = $('#comment').val();
        var name_help = $('#NamelHelp');
        var mail_help = $('#emailHelp');
        var massage_help =$('#textHelp');
    
        var check = true;
        
        if(!/^[a-zA-Zа-яА-Я]+$/.test(name)){
            name_help.text("Не допустимые символы");
            check = false;
            if(name == ""){
                name_help.text("Укажите имя");
                check = false;
            }
        }
        else name_help.text("");
        if(mail == ""){
            mail_help.text("Укажите Email");
            check = false; 
        }
        else mail_help.text("");
        if(massage == ""){
            massage_help.text("Введите сообщение");
            check = false;                                     
        }
        else massage_help.text("");
        if(!check){
            e.preventDefault();
        }
        else $("#report-modal").modal();
		
});