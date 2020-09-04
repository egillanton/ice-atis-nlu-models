if [ -d "sample_data" ]; then rm -rf sample_data; fi

if [ ! -d "ice-atis" ]; then git clone -l -s git://github.com/egillanton/ice-atis.git ice-atis > /dev/null 2>&1; fi