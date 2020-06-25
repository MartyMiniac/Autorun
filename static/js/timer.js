var timeLeft = 60;
    var elem = document.getElementById('time');
    var timerId = setInterval(countdown, 1000);

    function countdown() {
        if (timeLeft == -1) {
            clearTimeout(timerId);
            doSomething();
        } else {
            console.log(timeLeft)
            elem.innerHTML = timeLeft + ' seconds remaining';
            timeLeft--;
        }
    }

    function doSomething() {
        alert("Hi");
    }