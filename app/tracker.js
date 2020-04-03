$('button#expand-btn').click(function(){
    $('button').toggleClass('active');
    $('.title').toggleClass('active');
    $('nav').toggleClass('active');
  });

$('button#next-btn-1').click(function(){
    $('div.contact-area').toggleClass('d-none')
    $('div.contact-area2').toggleClass('d-none')
});
$('button#prev-btn-2').click(function(){
    $('div.contact-area').toggleClass('d-none')
    $('div.contact-area2').toggleClass('d-none')
});
$('button#next-btn-2').click(function(){
    $('div.contact-area2').toggleClass('d-none')
    $('div.contact-area3').toggleClass('d-none')
});
$('button#prev-btn-3').click(function(){
    $('div.contact-area3').toggleClass('d-none')
    $('div.contact-area2').toggleClass('d-none')
});

document.addEventListener('DOMContentLoaded', function(){
    downloadCovidData();
    function hide_footer(){
        $('#twitter-widget-0').contents().find('footer').hide();
        $('#twitter-widget-0').contents().find('.timeline-InformationCircle').hide();
        window.setTimeout(hide_footer, 1000);
    }
    hide_footer();

    function runModal1(){
        var modal = document.getElementById("popup-modal");

        var btn = document.getElementById("change-loc-btn");
        var btn2 = document.getElementById("change-loc-submit");

        var span = document.getElementById("popup-close-btn");

        btn.onclick = function() {
        modal.style.display = "block";
        }
        btn2.onclick = function() {
            modal.style.display = "none";
        }

        span.onclick = function() {
        modal.style.display = "none";
        }
    }
    function runModal2(){
        var modal = document.getElementById("popup-modal2");

        var btn = document.getElementById("about-btn");

        var span = document.getElementById("popup-close-btn2");

        btn.onclick = function() {
        modal.style.display = "block";
        }

        span.onclick = function() {
        modal.style.display = "none";
        }
    }
    function runModal3(){
        var modal = document.getElementById("popup-modal3");

        var btn = document.getElementById("ackno-btn");

        var span = document.getElementById("popup-close-btn3");

        btn.onclick = function() {
        modal.style.display = "block";
        }

        span.onclick = function() {
        modal.style.display = "none";
        }
    }
    runModal1();
    runModal2();
    runModal3();

    $('#change-loc-submit').click(function(){
        console.log('hello');
        var new_loc = $('#loc-select').val();
        setLocation(new_loc);
        setCovidValues(new_loc);
    })
},false)

//==========================================
function setLocation(location){
    chrome.storage.sync.clear();
    chrome.storage.sync.set({'covid_location': location}, function() {
        console.log(key + " is set to " + location);
    });
}

function downloadCovidData(){
    key='covid_location';
    chrome.storage.sync.get({"covid_location":"Hertfordshire"}, function(result) {
        var location = result[key];
        console.log(key +' currently is '+ location);
        setCovidValues(location);
    });
}

function setCovidValues(location){
    const url='https://j1ryxp2q26.execute-api.eu-west-2.amazonaws.com/default/covidDataUpdater';
    const query_data = JSON.stringify({county:location,query:"*"});
    console.log('heeey')
    $.post(url, query_data, function(data){
        console.log(data)
        var data_dict = JSON.parse(data.body);
        var places = data_dict['places'];
        $($('#loc-label')[0]).html(location);
        document.getElementById('loc-label').title = location
        $($('h1#case_count')[0]).html(data_dict['casecount']);
        $($('h1#uk-case-count')[0]).html(data_dict['TotalUKCases']);
        $($('h1#uk-death-count')[0]).html(data_dict['TotalUKDeaths']);
        $($('h1#uk-new-count')[0]).html(data_dict['NewUKCases']);
        $($('#loc-select')).empty();
        $.each(places, function(index, value){
            $($('#loc-select')).append("<option>"+value+"</option>");
        });
    });
}