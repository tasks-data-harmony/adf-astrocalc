<script>
  function convertToAbysmalCalendar(dateString) {
      let date = new Date(dateString);
      let epochStart = new Date("1492-05-26");
      let daysSinceEpoch = Math.floor((date - epochStart) / (1000 * 60 * 60 * 24));
      
      let abysmalYear = Math.floor(daysSinceEpoch / 365);
      let daysInCurrentYear = daysSinceEpoch % 365;

      // Check for New Year's Day (Winter Solstice)
      let winterSolstice = new Date(date.getFullYear(), 11, 21); // Dec 21 of that year
      if (date.toDateString() === winterSolstice.toDateString()) {
          return `${abysmalYear + 1} ♆`;  // Year rolls over!
      }

      // Check for Abyssal Leap Day (occurs after NYD every 4 years)
      let isLeapYear = ((abysmalYear + 1) % 4 === 0) && ((abysmalYear + 1) % 128 !== 0);
      let leapDay = new Date(date.getFullYear(), 11, 22); // Dec 22 (if applicable)
      if (isLeapYear && date.toDateString() === leapDay.toDateString()) {
          return `${abysmalYear + 1} ⛢`;  // Year stays rolled over!
      }

      // Adjust year if we're past NYD
      if (date > winterSolstice) {
          abysmalYear += 1;
      }

      // Calculate Month & Day
      let adjustedDay = daysInCurrentYear - (isLeapYear ? 1 : 0);
      let month = Math.floor(adjustedDay / 28) + 1;
      let day = (adjustedDay % 28) + 1;

      // Define celestial weekdays
      let weekdays = ["♄", "☉", "☽", "♂", "☿", "♃", "♀"];
      let weekdayIndex = (daysSinceEpoch - (abysmalYear * 365)) % 7;
      let weekday = weekdays[weekdayIndex];

      // Apply strikethrough formatting to month
      let strikethroughMonth = " " + month + " ";
      strikethroughMonth = strikethroughMonth.split("").map(char => char + "\u0336").join("");

      return `${abysmalYear} ~${strikethroughMonth}~ ${day} ${weekday}`;
  }

  document.addEventListener("DOMContentLoaded", function () {
      document.querySelectorAll(".abysmal-date").forEach(function (el) {
          el.innerText = convertToAbysmalCalendar(el.dataset.date);
      });
  });
</script>
