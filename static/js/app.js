function triggerFeedbackMessages(message) {

    switch (message.category) {
        case "register": popupFeedback(); break;
        case "login": mixinFeedback(); break;
        case "logout": mixinFeedback(); break;
        case "password_change": mixinFeedback(); break;
    }

    function popupFeedback() {
        var options = {
            text: message.text,
            icon: message.icon,
            timer: 3000,
        }

        if (message.title)
            options.title = message.title;

        Swal.fire(options);
    }

    function mixinFeedback() {
        Swal.mixin({
            toast: true,
            position: "top",
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            didOpen: (toast) => {
                toast.onmouseenter = Swal.stopTimer;
                toast.onmouseleave = Swal.resumeTimer;
            },
        }).fire({
            title: message.text,
            icon: message.icon,
            customClass: "animate__animated",
            showClass: {
                popup: "animate__bounceInDown"
            },
            hideClass: {
                popup: "animate__bounceOutUp"
            },
        });
    }
}