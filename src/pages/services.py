import streamlit as st

st.title("Services")

# HTML content with the Stripe pricing table
html_content = """
<!DOCTYPE html>
<html lang="en">
<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1PnKa400vggv2sUBuGVejI7l"
  publishable-key="pk_live_51PnIm700vggv2sUBL882Mfg4Mz41ZRhVL8dsESZym4FPG0YOn5UEzaD4qoGLvBdgoKuYiSFdyiE0jbmhKZq2HHdi00LgSLT3ht"
>
</stripe-buy-button>

<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1PnKpJ00vggv2sUB9VdrpSrz"
  publishable-key="pk_live_51PnIm700vggv2sUBL882Mfg4Mz41ZRhVL8dsESZym4FPG0YOn5UEzaD4qoGLvBdgoKuYiSFdyiE0jbmhKZq2HHdi00LgSLT3ht"
>
</stripe-buy-button>
</html>
"""

# Use Streamlit's HTML component to render the HTML content
st.components.v1.html(html_content, height = 1000, width = 1000)
