// JavaScript Document


$(window).on('load', function() {

	"use strict";

					
	/*----------------------------------------------------*/
	/*	Preloader
	/*----------------------------------------------------*/
	
	var preloader = $('#loader-wrapper'),
		loader = preloader.find('.cssload-loader');
		loader.fadeOut();
		preloader.delay(400).fadeOut('slow');
			
});


$(window).on('scroll', function() {
	
	"use strict";

							
	/*----------------------------------------------------*/
	/*	Navigtion Menu Scroll
	/*----------------------------------------------------*/	
	
	var b = $(window).scrollTop();
	
	if( b > 80 ){		
		$(".wsmainfull").addClass("scroll");
	} else {
		$(".wsmainfull").removeClass("scroll");
	}				

});


$(document).ready(function() {
		
	"use strict";


	/*----------------------------------------------------*/
	/*	Animated Scroll To Anchor
	/*----------------------------------------------------*/
	
	$('.header a[href^="#"], .wsmenu a[href^="#"], .page a.btn[href^="#"], .page a.internal-link[href^="#"]').on('click', function (e) {
		
		e.preventDefault();

		var target = this.hash,
			$target = jQuery(target);

		$('html, body').stop().animate({
			'scrollTop': $target.offset().top - 60 // - 200px (nav-height)
		}, 'slow', 'easeInSine', function () {
			window.location.hash = '1' + target;
		});
		
	});


	/*----------------------------------------------------*/
	/*	ScrollUp
	/*----------------------------------------------------*/
	
	$.scrollUp = function (options) {

		// Defaults
		var defaults = {
			scrollName: 'scrollUp', // Element ID
			topDistance: 600, // Distance from top before showing element (px)
			topSpeed: 800, // Speed back to top (ms)
			animation: 'fade', // Fade, slide, none
			animationInSpeed: 200, // Animation in speed (ms)
			animationOutSpeed: 200, // Animation out speed (ms)
			scrollText: '', // Text for element
			scrollImg: false, // Set true to use image
			activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
		};

		var o = $.extend({}, defaults, options),
			scrollId = '#' + o.scrollName;

		// Create element
		$('<a/>', {
			id: o.scrollName,
			href: '#top',
			title: o.scrollText
		}).appendTo('body');
		
		// If not using an image display text
		if (!o.scrollImg) {
			$(scrollId).text(o.scrollText);
		}

		// Minium CSS to make the magic happen
		$(scrollId).css({'display':'none','position': 'fixed','z-index': '99999'});

		// Active point overlay
		if (o.activeOverlay) {
			$("body").append("<div id='"+ o.scrollName +"-active'></div>");
			$(scrollId+"-active").css({ 'position': 'absolute', 'top': o.topDistance+'px', 'width': '100%', 'border-top': '1px dotted '+o.activeOverlay, 'z-index': '99999' });
		}

		// Scroll function
		$(window).on('scroll', function(){	
			switch (o.animation) {
				case "fade":
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).fadeIn(o.animationInSpeed) : $(scrollId).fadeOut(o.animationOutSpeed) );
					break;
				case "slide":
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).slideDown(o.animationInSpeed) : $(scrollId).slideUp(o.animationOutSpeed) );
					break;
				default:
					$( ($(window).scrollTop() > o.topDistance) ? $(scrollId).show(0) : $(scrollId).hide(0) );
			}
		});

		// To the top
		$(scrollId).on('click', function(event){
			$('html, body').animate({scrollTop:0}, o.topSpeed);
			event.preventDefault();
		});

	};
	
	$.scrollUp();


	/*----------------------------------------------------*/
	/*	Accordion
	/*----------------------------------------------------*/

	$(".accordion > .accordion-item.is-active").children(".accordion-panel").slideDown();
			
	$(".accordion > .accordion-item").click(function() {
		$(this).siblings(".accordion-item").removeClass("is-active").children(".accordion-panel").slideUp();
		$(this).toggleClass("is-active").children(".accordion-panel").slideToggle("ease-out");
	});

	
	/*----------------------------------------------------*/
	/*	Single Image Lightbox
	/*----------------------------------------------------*/
			
	$('.image-link').magnificPopup({
		type: 'image'
	});	


	/*----------------------------------------------------*/
	/*	Video Link #1 Lightbox
	/*----------------------------------------------------*/
	
	$('.video-popup1').magnificPopup({
		type: 'iframe',		  	  
			iframe: {
				patterns: {
					youtube: {			   
						index: 'youtube.com',
						src: 'https://www.youtube.com/embed/SZEflIVnhH8'				
							}
						}
					}		  		  
	});


	/*----------------------------------------------------*/
	/*	Video Link #2 Lightbox
	/*----------------------------------------------------*/
	
	$('.video-popup2').magnificPopup({
		type: 'iframe',		  	  
			iframe: {
				patterns: {
					youtube: {			   
						index: 'youtube.com',
						src: 'https://www.youtube.com/embed/7e90gBu4pas'				
							}
						}
					}		  		  
	});


	/*----------------------------------------------------*/
	/*	Video Link #3 Lightbox
	/*----------------------------------------------------*/
	
	$('.video-popup3').magnificPopup({
		type: 'iframe',		  	  
			iframe: {
				patterns: {
					youtube: {			   
						index: 'youtube.com',
						src: 'https://www.youtube.com/embed/0gv7OC9L2s8'					
							}
						}
					}		  		  
	});


	/*----------------------------------------------------*/
	/*	Statistic Counter
	/*----------------------------------------------------*/

	$('.count-element').each(function () {
		$(this).appear(function() {
			$(this).prop('Counter',0).animate({
				Counter: $(this).text()
			}, {
				duration: 4000,
				easing: 'swing',
				step: function (now) {
					$(this).text(Math.ceil(now));
				}
			});
		},{accX: 0, accY: 0});
	});


	/*----------------------------------------------------*/
	/*	Testimonials Rotator
	/*----------------------------------------------------*/

	var owl = $('.reviews-wrapper');
		owl.owlCarousel({
			items: 3,
			loop:true,
			autoplay:true,
			navBy: 1,
			autoplayTimeout: 4500,
			autoplayHoverPause: true,
			smartSpeed: 1500,
			responsive:{
				0:{
					items:1
				},
				767:{
					items:1
				},
				768:{
					items:2
				},
				991:{
					items:3
				},
				1000:{
					items:3
				}
			}
	});


	/*----------------------------------------------------*/
	/*	Brands Logo Rotator
	/*----------------------------------------------------*/

	var owl = $('.brands-carousel');
		owl.owlCarousel({
			items: 5,
			loop:true,
			autoplay:true,
			navBy: 1,
			nav:false,
			autoplayTimeout: 4000,
			autoplayHoverPause: false,
			smartSpeed: 2000,
			responsive:{
				0:{
					items:2
				},
				550:{
					items:3
				},
				767:{
					items:3
				},
				768:{
					items:4
				},
				991:{
					items:5
				},				
				1000:{
					items:6
				}
			}
	});


	/*----------------------------------------------------*/
	/*	Register Form Validation
	/*----------------------------------------------------*/
	
	$(".register-form").validate({
		rules:{ 
				name:{
					required: true,
					minlength: 2,
					maxlength: 16,
				},
				email:{
					required: true,
					email: true,
				},
				phone:{
					required: true,
					digits: true,
					}
				},
				messages:{
						name:{
							required: "Please enter no less than (1) characters"
						}, 
						email:{
							required: "We need your email address to contact you",
							email: "Your email address must be in the format of name@domain.com"
						}, 
						phone:{
							required: "Please enter only digits",
							digits: "Please enter a valid number"
						}, 
					}
	});


	/*----------------------------------------------------*/
	/*	Contact Form Validation
	/*----------------------------------------------------*/
	
	$(".contact-form").validate({
		rules:{ 
				name:{
					required: true,
					minlength: 1,
					maxlength: 16,
				},
				email:{
					required: true,
					email: true,
				},       		
				message:{
					required: true,
					minlength: 2,
					}
				},
				messages:{
						name:{
							required: "Please enter no less than (1) characters"
						}, 
						email:{
							required: "We need your email address to contact you",
							email: "Your email address must be in the format of name@domain.com"
						}, 
						message:{
							required: "Please enter no less than (2) characters"
						}, 
					}
	});


	/*----------------------------------------------------*/
	/*	Comment Form Validation
	/*----------------------------------------------------*/
	
	$(".comment-form").validate({
		rules:{ 
				name:{
					required: true,
					minlength: 1,
					maxlength: 16,
				},
				email:{
					required: true,
					email: true,
				},       		
				message:{
					required: true,
					minlength: 2,
					}
				},
				messages:{
						name:{
							required: "Please enter no less than (1) characters"
						}, 
						email:{
							required: "We need your email address to contact you",
							email: "Your email address must be in the format of name@domain.com"
						}, 
						message:{
							required: "Please enter no less than (2) characters"
						}, 
					}
	});	


	/*----------------------------------------------------*/
	/*	Newsletter Subscribe Form
	/*----------------------------------------------------*/

	$('.newsletter-form').ajaxChimp({
	language: 'cm',
	url: 'https://dsathemes.us3.list-manage.com/subscribe/post?u=af1a6c0b23340d7b339c085b4&id=344a494a6e'
		//http://xxx.xxx.list-manage.com/subscribe/post?u=xxx&id=xxx
	});

	$.ajaxChimp.translations.cm = {
		'submit': 'Submitting...',
		0: 'We have sent you a confirmation email',
		1: 'Please enter your email address',
		2: 'An email address must contain a single @',
		3: 'The domain portion of the email address is invalid (the portion after the @: )',
		4: 'The username portion of the email address is invalid (the portion before the @: )',
		5: 'This email address looks fake or invalid. Please enter a real email address'
	};	


});

$(document).ready(function () {
	$('#post_form').submit(function(i){
		i.preventDefault();

		post_form = $(this);

		var formData = new FormData();

		var serializedData = post_form.serializeArray();

		$.each(serializedData, function(i, field) {
			formData.append(field.name, field.value);
		});

		// Append file separately
		var fileInput = post_form.find('#id_file')[0].files[0];
		if (fileInput) {
			formData.append('file', fileInput);
		}

		$.ajax({
			method:'POST',
			url: post_form.attr('action'),
			data: formData,
			processData: false,
			contentType: false,
			success: function (response, django_backend, form_isbound) {
				post_form.trigger('reset');
				// console.log(serializedData);
				// console.log(response);
				// console.log(django_backend);
				// console.log(form_isbound);
				alert("done!");
				},
			error: function (response) {
				alert(response["responseJSON"]["error"]);
			}
		})
	})
})