
function FetchData() {

    fetch('api/data') // call api from django url

        .then(response => response.json())
        .then(data => {

            // let display_data = document.getElementById ('fetch_Data_Display').textContent = ""; // clear datas

            if (data.data.length > 0) {

                let Generate_random = data.data [Math.floor(Math.random() * data.data.length)];
                
                document.getElementById ('fetch_Data_Display').textContent = Generate_random.MainVerse;

            }else {

                document.getElementById ('fetch_Data_Display').textContent = "No Data Available!";

            }

        })

        .catch (error => console.error("Error fetching data:", error));

}

    setInterval (FetchData, 5000)

    FetchData();