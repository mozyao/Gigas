package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.Default()
	r.GET("/weather_info/:city", func(c *gin.Context) {
		city := c.Param("city")
		rsp := fetchWeather(city)
		c.JSON(200, rsp)
	})
	r.Run(":8080")
}
