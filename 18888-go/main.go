package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/guonaihong/gout"
)

type rsp struct {
	CityName string `json:"city_name,omitempty"`
	Date     string `json:"date,omitempty"`
	Humidity string `json:"humidity,omitempty"`
	PM25     int64  `json:"pm_25,omitempty"`
	PM10     int64  `json:"pm_10,omitempty"`
	Degree   int64  `json:"degree,omitempty"`
	Message  string
}

func main() {
	r := gin.Default()
	url := "http://18888-python:5000/weather_info"
	r.GET("/weather_info/:city_name", func(c *gin.Context) {
		rsp := rsp{}
		err := gout.GET(url).
			Debug(true).
			SetJSON(gout.H{
				"city_name": c.Param("city_name"),
			}).
			BindJSON(&rsp).
			Do()
		if err != nil {
			fmt.Printf("err = %v\n", err)
		} else {
			if rsp.CityName != "" {
				rsp.Message = fmt.Sprintf("City is %s, Date is %s, Degree is %d celsius, Humidity is %s, pm 2.5 is %d, pm 10 is %d",
					rsp.CityName, rsp.Date, rsp.Degree, rsp.Humidity, rsp.PM25, rsp.PM10)
			}
		}
		c.JSON(200, rsp)
	})
	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
