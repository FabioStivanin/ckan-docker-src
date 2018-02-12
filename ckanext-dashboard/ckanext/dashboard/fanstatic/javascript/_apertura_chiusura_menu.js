//console.log('my javascript per APERTURA/ CHIUSURA MENU APPLICAZIONI e STRUTTURE RIFERIMENTO');

if (apri > 5) {

		$(".colla").click(function () {

										$colla = $(this);
										//getting the next element
										$aprilo_full = $colla.next();

										$aprilo = $colla.prev();
										//open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
										$aprilo_full.slideToggle(function () {

											//execute this after slideToggle is done
											//change text of header based on visibility of content div
											$colla.text(function () {
												//change text based on condition
												return $aprilo_full.is(":visible") ? "Nascondi secondarie" : "Mostra di più";
											});
										});

									});
								}
								else {
									$(".colla").text("Nessun'altra applicazione disponibile");
								}
;







if (data3.count > 5) {
				$(".colla2").click(function () {

										$colla = $(this);
										//getting the next element
										$aprilo_full = $colla.next();

										$aprilo = $colla.prev();
										//open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
										$aprilo_full.slideToggle(function () {

											//execute this after slideToggle is done
											//change text of header based on visibility of content div
											$colla.text(function () {
												//change text based on condition
												return $aprilo_full.is(":visible") ? "Nascondi secondarie" : "Mostra di più";
											});
										});

									});
								}
								else {
									$(".colla2").text("Nessun'altra struttura disponibile");
								}
;
