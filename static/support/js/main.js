/*  Framework: JQUERRY
    AJAX: 
        -GET - FAQ
        -POST - Feedback
*/
var $=jQuery.noConflict();
function listfaq(){
    $.ajax({
        url:"/support/faq_list/",
        type:"get",
        dataType:"json",
        success:function(response){
            $('#faq1').html("");
            for (let i=0; i<response.length;i++){
                
                let parrafo = "<h2>" + response[i]["fields"]["question"] + "</h2>";
                parrafo += "<p>" + response[i]["fields"]["answer"] + "</p>";
                parrafo += "<p>" + response[i]["fields"]["image"] + "</p>";
                $("#faq1").append(parrafo);
            }
            
        },
        error: function(error){
            console.log(error);
        }
    });
}

function createFeedBack(){
    $.ajax({
        data: $("#form_feedback").serialize(),
        url: $("#form_feedback").attr("action"),
        type: $("#form_feedback").attr("method"),
        
        success: function(response){
            console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    })    
}


//Invocar función
$(document).ready(function (){
    listfaq();
})


