#!/usr/bin/env ruby

require 'fileutils'

class BuildZip

  def self.run

    # remove any previous zip file
    Dir['ht*.zip'].each {|file| FileUtils.rm_rf file }

    Dir['*'].each do |dir|
      next unless File.directory? dir
      next if dir.start_with? '.'

      zipfile = dir[0..(dir.rindex('-')-1)]
      puts zipfile

      Dir.chdir dir
      system "zip -r ../#{zipfile}.zip *"
      Dir.chdir '..'

    end
  end

end

if __FILE__ == $0
  BuildZip.run
end