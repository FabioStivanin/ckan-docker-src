

var fill = d3.scale.category10(); 
// scala i colori della cloud 
// https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#categorical-colors


//var color = d3.scale.linear()
		//.domain([0, 1, 2, 3, 4, 5, 6, 10, 15, 20, 100])
		//.range(["#ddd", "#ccc", "#bbb", "#aaa", "#999", "#888", "#777", "#666", "#555", "#444", "#333", "#222"]);


function draw(words) {

	d3.select("#cloud").append("svg") //where to insert the cloud
				.attr("width", w)
					.attr("height", h)
						.append("g")
						.attr("transform", "translate(" + w / 2 + "," + h / 2 + ")")
							.selectAll("text")
							.data(words)
							.enter().append("text")
							.style("font-size", function (d) { return (d.size) + "px"; })
							.style("font-family", "Impact")
							.style("fill", function (d, i) { return fill(i); })
							.attr("text-anchor", "middle")
							.attr("transform", function (d) {
								return "translate(" + [1.1*d.x, 1.3*d.y] + ")rotate(" + d.rotate + ")";
							})
							.text(function (d) { return d.text; })
							.on("mouseover", function (d) {
								d3.select(this).style("cursor", "pointer")
							})
							.on("click", function (d, i) {
								window.open("dataset?q=tags%3A\"" + d.text + "\"", '_self', false);
				});
		}

		
var maxximo = frequency_list[0].size;



if (user != "" && user != "opendata_member") {
						d3.layout.cloud().size([w, h])
							.words(frequency_list)
							.padding(0.01 * w)
							.rotate(function (d) { return ~~(0.2 * 2) * 90; })
							//    .font("Impact")
							.text(function (d) { return d.text; })
							.fontSize(function (d) { return Math.sqrt(d.size * 5); })
							.on("end", draw)
							.start();
					}
					else {

						d3.layout.cloud().size([w, h])
							.words(frequency_list)
							.padding(0.01 * w)
							.rotate(function (d) { return ~~(0.2 * 2) * 90; })
							//    .font("Impact")
							.text(function (d) { return d.text; })
							.fontSize(function (d) { 
								if (maxximo<8 ){
								return Math.sqrt(d.size * 200);}
									else {
									return Math.sqrt(d.size * 40);
									}
									 })
							.on("end", draw)
							.start();

					}

					
