var main = function () {
    
    $(".friends-button").click(
        function(){
            
            $('.menu').animate({
                right: "0px"
            }, 300);
        
            
            $('body').animate({
                right: "250px"
            }, 300);
        }
    );
}

$(document).ready(main);