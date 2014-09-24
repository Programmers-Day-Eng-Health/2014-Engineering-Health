require 'net/http'
require 'uri'
require 'json'
require 'pp'
uri = URI('http://www.eventbrite.com/json/event_search?')
if(ARGV.count == 2)
	uri.query <<  URI.encode_www_form({:keyword => ARGV[0], :city => ARGV[1], :app_key => '6AQYIANBMA2JSZNBS2'})
	http = Net::HTTP.start(uri.host, uri.port)
	response = JSON.parse(http.request_get(uri).body)
	if(response.has_key?("events"))
		response["events"].each do |event|
			event.each do |key, value|
				if(key == 'summary')
					puts "Summay: Total Events #{value['total_items']}, Showing Events #{value['num_showing']}\n\n"
				elsif(key == 'event')
					description = value['description'].gsub(/<\/?[^>]*>/, '').gsub(/\n\n+/, "\n").gsub(/^\n|\n$/, '')
					puts "******************************************************************* \nOrganizer: #{value['organizer']['name']} \nDate: #{value['start_date']} \nDescripiton: #{description}\nAddress: #{value['venue']['address']} #{value['address_2']} \n\n"
						
				end
			end		
		end		
	end
else
	puts 'Incorrect format!! Run script with the relevent keyword and city'
end	

