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
    const url='https://j1ryxp2q26.execute-api.eu-west-2.amazonaws.com/default/covidDataUpdater';
    const query_data = JSON.stringify({county:"Suffolk",query:"*"});
    $.post(url, query_data, function(data){
        var data_dict = JSON.parse(data.body);
        $($('h1#case_count')[0]).html(data_dict['casecount']);
        $($('h1#uk-case-count')[0]).html(data_dict['TotalUKCases']);
        $($('h1#uk-death-count')[0]).html(data_dict['TotalUKDeaths']);
        $($('h1#uk-new-count')[0]).html(data_dict['NewUKCases']);
    });
    function hide_footer(){
        $('#twitter-widget-0').contents().find('footer').hide();
        $('#twitter-widget-0').contents().find('.timeline-InformationCircle').hide();
        window.setTimeout(hide_footer, 1000);
    }
    hide_footer();
},false)
//==========================================