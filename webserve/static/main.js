var ctx = document.getElementById("myChart");
var emisPlot = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: '# of Votes',
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
    let livefeed = document.getElementById('livefeed');
    let startTime = document.getElementById('startTime');
    let startDate = document.getElementById('startDate');
    let startHrs = startTime.valueAsDate.getUTCHours()
    let startMins = startTime.valueAsDate.getUTCMinutes()
    var start = new Date(startDate);
    start.setHours(startHrs);start.setMinutes(startMins);
    device = 'abc';
    if (livefeed.checked != true){
        let endDate = document.getElementById('endDate');
        let endTime = document.getElementById('endTime');
        let endHrs = endTime.valueAsDate.getUTCHours()
        let endMins = endTime.valueAsDate.getUTCMinutes()
        var end = new Date(endDate);
        end.setHours(endHrs);end.setMinutes(endMins);
        datagrab(device,start,end);
    }else{
        live_update(device,start);
    }

}

function datagrab(device,start,end){
    var xmlhttp = new XMLHttpRequest();
    var url = "/api/live";
    xmlhttp.open("GET", url, true);
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var returned_data = JSON.parse(this.responseText);
            plot_set(returned_data);
        }
    }
    xmlhttp.send();
}
 

function plot_update(time,point){
    //time as a date object 
    //point as a value
    emisPlot.data.datasets[0].data.push({x:time,y: point});
    emisPlot.update();
}

function plot_set(returned_data){
    console.log(returned_data);
    plotting_data = returned_data.map(value =>{
        return {x:new Date(value.timestamp),y:value.level};
    })
    emisPlot.data.datasets[0].data = plotting_data;
    console.log(plotting_data);
    emisPlot.update();
}


function live_update(device,start){
    var end = new Date();
    datagrab(device,start,end)
};
    
var updateTimer;
function startUpdate(){
    updateTimer = setInterval(demo_update, 5000);
}
function stopUpdate(){
    clearInterval(updateTimer);
}
