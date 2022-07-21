if($('.criminal-form')){
    const textInputs = document.querySelectorAll('.text-input');
    const textErrorArea = document.querySelectorAll('.text-error-area');

    var validityCheck = [];
    $(textInputs).each(function (index,item){
        validityCheck.push({index:index,valid:false})
    });
    var counter = validityCheck.length
    $(textInputs).each(function (index,item){
        $(item).keyup(function () {
             if (validateText($(item), $(textErrorArea[index]))) {
                 validityCheck[index].valid = true
             } else {
                 validityCheck[index].valid = false
             }
             console.log(validityCheck)
         });
    });
    validityCheck.push({index:(counter),valid:false});
    $('.text-tel').keyup(function (){
        if (validateTel($(this), $('.tel-error-area'))) {
            validityCheck[counter].valid =true;
        } else {
            validityCheck[counter].valid =false;
        }
        console.log(validityCheck)
    });
    $(".submit-btn").click(function (e) {
            e.preventDefault();
            var allValid;
            validityCheck.forEach(function (item,index){
                if (item.valid === true) {
                    allValid = item.valid;
                }
            });
            if(allValid===true){
                $('.criminal-form').submit();
            }
        });
}
