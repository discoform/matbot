function dragMoveListener(t){var e=t.target,a=(parseFloat(e.getAttribute("data-x"))||0)+t.dx,r=(parseFloat(e.getAttribute("data-y"))||0)+t.dy;e.style.webkitTransform=e.style.transform="translate("+a+"px, "+r+"px)",e.setAttribute("data-x",a),e.setAttribute("data-y",r)}interact(".draggable").draggable({inertia:!0,modifiers:[interact.modifiers.restrictRect({restriction:"parent",endOnly:!0})],autoScroll:!0,onmove:dragMoveListener,onend:function(t){var e=t.target.querySelector("p");e&&(e.textContent="moved a distance of "+Math.sqrt(Math.pow(t.pageX-t.x0,2)+Math.pow(t.pageY-t.y0,2)|0).toFixed(2)+"px")}}),window.dragMoveListener=dragMoveListener;