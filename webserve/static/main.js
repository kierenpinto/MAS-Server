var ctx = document.getElementById("myChart");
var emisPlot = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Particulate Matter 2.5',
            data: [],
            fill:false,
            showLine: true,
            lineTension: 0
        },]
    },
    options: {
        title: {
            display: true,
            text: 'MonashAirSense'
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
            xAxes: [{
                type: 'time',
                time: {
                    
                },
                displayFormats: {
                    quarter: 'MMM YYYY'
                }
            }]
        },
        legend:{
            display:false
        }
    },
    maintainAspectRatio: false,
});

function settingsUpdate(){
    var livefeed = document.getElementById('livefeed');
    var startTime = document.getElementById('startTime');
    var startDate = document.getElementById('startDate');
    var startHrs = startTime.valueAsDate.getUTCHours()
    var startMins = startTime.valueAsDate.getUTCMinutes()
    var start = new Date(startDate.valueAsDate);
    start.setHours(startHrs);start.setMinutes(startMins);
    console.log(start);
    device = 'abc';
    if (livefeed.checked != true){
        var endDate = document.getElementById('endDate');
        var endTime = document.getElementById('endTime');
        var endHrs = endTime.valueAsDate.getUTCHours()
        var endMins = endTime.valueAsDate.getUTCMinutes()
        var end = new Date(endDate.valueAsDate);
        end.setHours(endHrs);end.setMinutes(endMins);
        console.log(end)   
        if (typeof(updateTimer) =='number'){
            clearInterval(updateTimer);
        }
        datagrab(device,start.getTime(),end.getTime());
    }else{
        //live_update(device,start.getTime());
        updateTimer = setInterval(()=>{live_update(device,start.getTime())}, 3000);
    }

}

function datagrab(device,start,end){
    var xmlhttp = new XMLHttpRequest();
    var url = new URL(window.location.href+"api/query");
    url.searchParams.set('start_ts',start);
    url.searchParams.set('end_ts',end);
    xmlhttp.open("GET", url.href, true);
    console.log(url.href)
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var returned_data = JSON.parse(this.responseText);
            console.log(returned_data);
            plot_set(returned_data);
        }
    }
    xmlhttp.send();
    return
}
 

function plot_update(time,point){
    //time as a date object 
    //point as a value
    emisPlot.data.datasets[0].data.push({x:time,y: point});
    emisPlot.update();
    return;
}

function plot_set(returned_data){
    console.log(returned_data);
    plotting_data = returned_data.map(value =>{
        return {x:new Date(value.timestamp),y:value.level};
    })
    emisPlot.data.datasets[0].data = plotting_data;
    console.log(plotting_data);
    emisPlot.update();
    return;
}


function live_update(device,start){
    var end = new Date().getTime();
    datagrab(device,start,end);
    console.log(end)
    return;
};
    
//var updateTimer;

//clearInterval(updateTimer);
