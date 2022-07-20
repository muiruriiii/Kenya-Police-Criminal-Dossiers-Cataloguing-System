function showAlert(alertArea) {
    alertArea.show("slow");
    setTimeout(function () {
        alertArea.hide("slow");
    }, 3000);
}

function validateText(inputText, errorArea) {
    value = inputText.val()
    if (value.length < 3 || value.length >= 14) {
        //errorArea.html("Invalid "+ inputText.title +".");
        errorArea.removeClass("hidden");
        inputText.addClass("border-red-700");
        inputText.removeClass("border-green-500");
        return false;
    } else {
        var textReg = /^[A-Za-z _]*[A-Za-z][A-Za-z _]*$/;
        var is_valid = textReg.test(inputText.val());
        if (is_valid) {
            errorArea.addClass("hidden");
            inputText.removeClass("border-red-700");
            inputText.addClass("border-green-500");
            return true;
        } else {
            errorArea.removeClass("hidden");
            inputText.addClass("border-red-700");
            inputText.removeClass("border-green-500");
            return false;
        }
    }
}

function validateEmail(email, errorArea) {
    if (email.val().length <= 6) {
        errorArea.removeClass('hidden');
        email.addClass("border-red-700");
        email.removeClass("border-green-500");
    } else {
        var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
        var is_valid = emailReg.test(email.val());
        if (is_valid) {
            errorArea.addClass("hidden");
            email.removeClass("border-red-700");
            email.addClass("border-green-500");
            return true;
        } else {
            errorArea.removeClass("hidden");
            email.addClass("border-red-700");
            email.removeClass("border-green-500");
            return false;
        }
    }
}
function validateTel(telno, errorArea) {
    if (telno.val().length <= 6) {
        errorArea.removeClass('hidden');
        telno.addClass("border-red-700");
        telno.removeClass("border-green-500");
    } else {
        var telnoReg = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
        var is_valid = telnoReg.test(telno.val());
        if (is_valid) {
            errorArea.addClass("hidden");
            telno.removeClass("border-red-700");
            telno.addClass("border-green-500");
            return true;
        } else {
            errorArea.removeClass("hidden");
            telno.addClass("border-red-700");
            telno.removeClass("border-green-500");
            return false;
        }
    }
}
