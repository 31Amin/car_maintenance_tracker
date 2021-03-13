$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.collapsible').collapsible();
    $('select').formSelect();
    $(".remove_item").hide();
    $('.tooltipped').tooltip();
    });

// Add / remove lines to service item list in add_record task.
$(".add_item").click(function () {
    $(".item").append(' <input placeholder="Add service line item" id="service_items" name="service_items" type="text" class="validate addtional_line"><label for="serviceservice_items_cost"></label> ');
    $(".remove_item").show();
    });

$(".remove_item").click(function () {
    $(".addtional_line").last().remove();
    });

$(".select_car").change(function() {
    var selected_car = $( "#reg_no" ).val();
    console.log(cars)
    });