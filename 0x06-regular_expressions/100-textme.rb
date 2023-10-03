#!/usr/bin/env ruby
sender=ARGV[0].scan(/from:\K\S+(?=])/).flatten.first
receiver=ARGV[0].scan(/to:\K\S+(?=])/).flatten.first
flags=ARGV[0].scan(/flags:\K\S+(?=])/).flatten.first
puts "#{sender},#{receiver},#{flags}"


# Other combinations
#from:\K\S+|to:\K{12}\S+|flags:\K\S{12,13}
#from:\K\S+|to:\K{12}\S+|flags:\K\S+
#from:\K\S+(?=])|to:\K\S+(?=])|flags:\K\S+(?=])