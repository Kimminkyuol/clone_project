function draw_bar(){
  var bars = document.querySelectorAll('.bar')

  var total = parseInt(bars[0].getAttribute('value'))

  for (let index = 0; index < bars.length; index++){
      console.log(100*parseInt(bars[index].getAttribute('value'))/total);
      bars[index].style.width = String(100*parseInt(bars[index].getAttribute('value'))/total)+'%';
  }
};

setTimeout(draw_bar, 1000);
