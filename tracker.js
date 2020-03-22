document.addEventListener('DOMContentLoaded', function(){
    document.addEventListener('button',onclick, false)

    function onclick () {
        $("label:contain('Suffolk:')").text = 'Yess';
    }
}, false)