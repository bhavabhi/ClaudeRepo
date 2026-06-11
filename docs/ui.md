# UI Standards Documentation

## Overview
This document outlines the UI standards and guidelines for the Calendar Application dashboard.

## Component Guidelines

### Allowed Components
Only **shadcn UI components** should be used throughout the application. This ensures consistency, maintainability, and a cohesive user experience.

### Prohibited Components
- Custom-built components
- Third-party UI libraries (except shadcn)
- Inline styled components without shadcn equivalents

## Design Principles

1. **Consistency**: All UI elements must follow shadcn design patterns
2. **Accessibility**: Components must be accessible and WCAG compliant
3. **Responsiveness**: All components must work on desktop, tablet, and mobile views
4. **Performance**: Use optimized shadcn components to maintain fast load times

## Date Formatting

All dates must be formatted using the **date-fns** library with **ordinal format**.

### Format Pattern
- **Pattern**: `d'${getOrdinalSuffix(d)}' MMM yyyy`
- **Examples**: 
  - 1st Sept 2026
  - 15th June 2026
  - 22nd December 2026

### Implementation
When displaying dates in the UI, use date-fns utilities:
```javascript
import { format } from 'date-fns';

// Ordinal formatting function
function getOrdinalSuffix(day) {
  if (day > 3 && day < 21) return 'th';
  return ['st', 'nd', 'rd'][day % 10 - 1] || 'th';
}

const formattedDate = format(new Date(), `d'${getOrdinalSuffix(date.getDate())}' MMM yyyy`);
```

## Color Palette

- **Primary**: #007bff (Blue)
- **Success**: #28a745 (Green)
- **Warning**: #ffc107 (Amber)
- **Danger**: #dc3545 (Red)
- **Background**: #f5f5f5 (Light Gray)
- **Text**: #333333 (Dark Gray)

## Typography

- **Headings**: 28px (h1), 18px (h2), 16px (h3)
- **Body**: 14px
- **Small**: 12px
- **Font Family**: System fonts (-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, etc.)

## Layout Guidelines

1. **Container**: Max-width of 1200px, centered on page
2. **Spacing**: Consistent 20px padding/margins
3. **Sections**: Clear visual separation with borders and background colors
4. **Daily View**: Default display mode showing events, tasks, and reminders

## Component Usage

### Button
- Use shadcn Button component for all interactive elements
- Primary buttons for main actions
- Secondary buttons for alternative actions

### Input
- Use shadcn Input component for date picker
- Ensure proper validation and error states

### Cards
- Use shadcn Card component for section containers
- Maintain consistent padding and spacing

### Lists
- Use semantic HTML with proper ARIA labels
- Implement keyboard navigation for accessibility

## Responsive Design

- **Desktop**: Full-width container with side-by-side layouts where applicable
- **Tablet**: Adjusted spacing and responsive grid layouts
- **Mobile**: Single-column layout with touch-friendly spacing

## Accessibility Requirements

- All interactive elements must be keyboard accessible
- Use semantic HTML (buttons, links, headings)
- Include ARIA labels for screen readers
- Maintain sufficient color contrast (WCAG AA standard)
- Support focus indicators and tab order

## Testing

Before deployment, ensure:
1. All components render correctly in shadcn theme
2. Date formatting matches ordinal pattern
3. Responsive design works on all breakpoints
4. Accessibility compliance is met
5. No custom components are used
